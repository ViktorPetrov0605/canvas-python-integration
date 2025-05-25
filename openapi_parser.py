#!/usr/bin/env python3
"""
OpenAPI Parser - Splits a large OpenAPI schema into smaller tools and generates 
Python code based on endpoint groups.

This script:
1. Parses an OpenAPI schema file
2. Groups endpoints by tags
3. Generates Python tool classes for each group
4. Creates subset OpenAPI schema files for each group
"""

import json
import os
import re
from typing import Dict, List, Optional, Set, Any
import argparse
from collections import defaultdict

# Template for the tool header
TOOL_HEADER_TEMPLATE = '''"""
title: {title} API Tool
author: Auto Generated
description: API Tool for interacting with {title} endpoints
required_open_webui_version: 0.5.0
requirements: requests
version: 0.1.0
licence: MIT
"""

import os
import requests
from typing import Dict, Any, List, Optional, Union
'''

# Template for the tool class
TOOL_CLASS_TEMPLATE = '''

class Tools:
    def __init__(self):
        """
        Initialize the Tools class with API configuration.
        Modify the API base URL and authentication as needed for your service.
        """
        # Get the base URL from environment variable or use default
        self.api_base = os.environ.get("API_BASE_URL", "http://localhost:8000")
        # Get the API key from environment variable if it exists
        api_key = os.environ.get("API_KEY", "")
        
        # Set up headers
        self.headers = {
            "Content-Type": "application/json",
        }
        
        # Add authorization if API key is provided
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
'''

# Template for method implementation
METHOD_TEMPLATE = '''
    def {method_name}(self, {method_params}) -> dict:
        """
        {summary}
        
        {description}
        
        {param_docs}
        :return: Dictionary with API response data or error details
        """
        url = self.api_base + f"{path_template}"
        
        {payload_code}
        
        try:
            method = "{http_method}".lower()
            if method == "get":
                response = requests.get(url{payload_arg}{query_param_arg}, headers=self.headers)
            elif method == "post":
                response = requests.post(url{payload_arg}{query_param_arg}, headers=self.headers)
            elif method == "put":
                response = requests.put(url{payload_arg}{query_param_arg}, headers=self.headers)
            elif method == "delete":
                response = requests.delete(url{payload_arg}{query_param_arg}, headers=self.headers)
            elif method == "patch":
                response = requests.patch(url{payload_arg}{query_param_arg}, headers=self.headers)
            else:
                response = requests.get(url{payload_arg}{query_param_arg}, headers=self.headers)
            
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {{
                "error": str(e),
                "status_code": getattr(response, "status_code", None),
                "text": getattr(response, "text", ""),
            }}
'''

def snake_case(name: str) -> str:
    """Convert a string to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def extract_params_from_schema(schema: Dict) -> List[Dict]:
    """Extract parameters from a schema."""
    params = []
    
    # Extract from parameters section
    if 'parameters' in schema:
        for param in schema['parameters']:
            param_info = {
                'name': param.get('name', ''),
                'required': param.get('required', False),
                'in': param.get('in', 'query'),
                'description': param.get('description', ''),
                'schema': param.get('schema', {}),
            }
            params.append(param_info)
            
    # Extract from requestBody if it exists
    if 'requestBody' in schema and 'content' in schema['requestBody']:
        for content_type, content in schema['requestBody']['content'].items():
            if 'schema' in content:
                body_schema = content['schema']
                # Handle schema reference
                if '$ref' in body_schema:
                    params.append({
                        'name': 'body',
                        'required': schema['requestBody'].get('required', False),
                        'in': 'body',
                        'description': 'Request body',
                        'schema': body_schema,
                    })
                # Handle inline schema
                else:
                    if 'properties' in body_schema:
                        for prop_name, prop_schema in body_schema['properties'].items():
                            required = prop_name in body_schema.get('required', [])
                            params.append({
                                'name': prop_name,
                                'required': required,
                                'in': 'body',
                                'description': prop_schema.get('description', f'{prop_name} parameter'),
                                'schema': prop_schema,
                            })
    
    return params

def get_type_hint(schema: Dict) -> str:
    """Get Python type hint from JSON schema."""
    if not schema:
        return 'Any'
        
    schema_type = schema.get('type')
    
    if schema_type == 'string':
        return 'str'
    elif schema_type == 'integer':
        return 'int'
    elif schema_type == 'number':
        return 'float'
    elif schema_type == 'boolean':
        return 'bool'
    elif schema_type == 'array':
        items_type = get_type_hint(schema.get('items', {}))
        return f'List[{items_type}]'
    elif schema_type == 'object':
        return 'Dict[str, Any]'
    else:
        return 'Any'

def generate_method_params(params: List[Dict], components: Dict) -> tuple:
    """Generate method parameters and documentation."""
    param_list = []
    param_docs = []
    payload_dict = {}
    query_params = {}
    
    for param in params:
        param_name = param['name']
        snake_name = snake_case(param_name)
        
        # Resolve schema reference if needed
        schema = param['schema']
        if '$ref' in schema:
            ref_path = schema['$ref'].split('/')
            if ref_path[1] == 'components' and ref_path[2] == 'schemas':
                schema_name = ref_path[3]
                if schema_name in components['schemas']:
                    schema = components['schemas'][schema_name]
        
        # Get type hint
        type_hint = get_type_hint(schema)
        
        # Add to parameter list
        if param['required']:
            param_list.append(f'{snake_name}: {type_hint}')
        else:
            param_list.append(f'{snake_name}: Optional[{type_hint}] = None')
        
        # Add to documentation
        param_docs.append(f':param {snake_name}: {param.get("description", "")}')
        
        # Track parameter for payload or query string
        if param['in'] == 'body':
            payload_dict[param_name] = snake_name
        elif param['in'] == 'query':
            query_params[param_name] = snake_name
        elif param['in'] == 'path':
            # Path parameters should be part of URL formatting
            pass
    
    # Join parameters with commas for method signature
    method_params_str = ', '.join(param_list)
    param_docs_str = '\n        '.join(param_docs)
    
    return method_params_str, param_docs_str, payload_dict, query_params

def generate_method(path: str, method: str, schema: Dict, components: Dict) -> str:
    """Generate a Python method for an API endpoint."""
    # Extract basic information
    operation_id = schema.get('operationId', f'{method}_{snake_case(path)}')
    method_name = snake_case(operation_id)
    summary = schema.get('summary', '')
    description = schema.get('description', 'No description provided')
    
    # Extract parameters
    all_params = extract_params_from_schema(schema)
    method_params, param_docs, payload_dict, query_params = generate_method_params(all_params, components)
    
    # Generate payload code
    if payload_dict:
        payload_lines = ["payload = {"]
        for api_name, param_name in payload_dict.items():
            payload_lines.append(f'            "{api_name}": {param_name},')
        payload_lines.append("        }")
        payload_code = '\n'.join(payload_lines)
        payload_arg = ", json=payload"
    else:
        payload_code = "# No payload required"
        payload_arg = ""
    
    # Generate query parameters
    if query_params:
        query_lines = ["params = {"]
        for api_name, param_name in query_params.items():
            query_lines.append(f'            "{api_name}": {param_name},')
        query_lines.append("        }")
        query_code = '\n'.join(query_lines)
        query_param_arg = ", params=params"
        # Add query_code to payload_code
        if payload_code:
            payload_code = payload_code + "\n        " + query_code
        else:
            payload_code = query_code
    else:
        query_param_arg = ""
    
    # Process path parameters
    path_template = path
    # Check for path parameters - replace {param} with {param_snake_case}
    for param in all_params:
        if param['in'] == 'path':
            param_name = param['name']
            snake_name = snake_case(param_name)
            path_template = path_template.replace(f"{{{param_name}}}", f"{{{snake_name}}}")
            
    # Return the formatted method template
    return METHOD_TEMPLATE.format(
        method_name=method_name,
        method_params=method_params,
        summary=summary,
        description=description,
        param_docs=param_docs,
        path_template=path_template,
        payload_code=payload_code,
        http_method=method.lower(),
        payload_arg=payload_arg,
        query_param_arg=query_param_arg
    )

def create_subset_openapi(
    tag: str,
    paths: Dict,
    components_schemas: Dict,
    original_info: Dict
) -> Dict:
    """Create a subset of the OpenAPI schema for the given tag."""
    # Start with a base structure
    openapi_subset = {
        "openapi": "3.1.0",
        "info": {
            "title": f"{tag.capitalize()} API",
            "version": original_info.get('version', '0.1.0'),
            "description": f"API endpoints for {tag}"
        },
        "paths": {},
        "components": {
            "schemas": {},
            "securitySchemes": {
                "HTTPBearer": {
                    "type": "http",
                    "scheme": "bearer"
                }
            }
        }
    }
    
    used_schemas: Set[str] = set()
    
    # Add paths for the specified tag
    for path, methods in paths.items():
        for method, operation in methods.items():
            operation_tags = operation.get('tags', [])
            if tag in operation_tags:
                # Add this path/method to our subset
                if path not in openapi_subset["paths"]:
                    openapi_subset["paths"][path] = {}
                openapi_subset["paths"][path][method] = operation
                
                # Track referenced schemas
                if 'requestBody' in operation and 'content' in operation['requestBody']:
                    for content_type, content_schema in operation['requestBody']['content'].items():
                        if 'schema' in content_schema and '$ref' in content_schema['schema']:
                            ref = content_schema['schema']['$ref']
                            if ref.startswith('#/components/schemas/'):
                                schema_name = ref.split('/')[-1]
                                used_schemas.add(schema_name)
                
                # Check responses for schema references
                if 'responses' in operation:
                    for response_code, response in operation['responses'].items():
                        if 'content' in response:
                            for content_type, content_schema in response['content'].items():
                                if 'schema' in content_schema and '$ref' in content_schema['schema']:
                                    ref = content_schema['schema']['$ref']
                                    if ref.startswith('#/components/schemas/'):
                                        schema_name = ref.split('/')[-1]
                                        used_schemas.add(schema_name)
    
    # Recursively add referenced schemas
    def add_ref_schemas(schema_name: str):
        if schema_name not in components_schemas:
            return
        
        # Add this schema
        openapi_subset["components"]["schemas"][schema_name] = components_schemas[schema_name]
        
        # Look for references within this schema
        schema = components_schemas[schema_name]
        refs = []
        
        # Check properties
        if 'properties' in schema:
            for prop_name, prop in schema['properties'].items():
                if '$ref' in prop:
                    ref = prop['$ref']
                    if ref.startswith('#/components/schemas/'):
                        refs.append(ref.split('/')[-1])
                elif prop.get('type') == 'array' and 'items' in prop:
                    if '$ref' in prop['items']:
                        ref = prop['items']['$ref']
                        if ref.startswith('#/components/schemas/'):
                            refs.append(ref.split('/')[-1])
        
        # Add all referenced schemas recursively
        for ref in refs:
            if ref not in openapi_subset["components"]["schemas"]:
                add_ref_schemas(ref)
    
    # Add all used schemas and their dependencies
    for schema_name in used_schemas:
        add_ref_schemas(schema_name)
    
    return openapi_subset

def process_openapi(openapi_file: str, output_dir: str):
    """Process an OpenAPI schema file and generate tools and subset schemas."""
    # Load the OpenAPI schema
    with open(openapi_file, 'r', encoding='utf-8') as f:
        openapi = json.load(f)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Group paths by tag
    paths_by_tag = defaultdict(dict)
    
    for path, methods in openapi['paths'].items():
        for method, operation in methods.items():
            tags = operation.get('tags', ['default'])
            for tag in tags:
                if path not in paths_by_tag[tag]:
                    paths_by_tag[tag] = {}
                if path not in paths_by_tag[tag]:
                    paths_by_tag[tag][path] = {}
                paths_by_tag[tag][path][method] = operation
    
    # Process each tag group
    for tag, paths in paths_by_tag.items():
        print(f"Processing tag: {tag}")
        
        # Create a Python tool file for this tag
        tool_file = os.path.join(output_dir, f"{tag.lower()}_tool.py")
        with open(tool_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write(TOOL_HEADER_TEMPLATE.format(title=tag.capitalize()))
            
            # Write class definition
            f.write(TOOL_CLASS_TEMPLATE)
            
            # Process each path/method
            for path in sorted(paths.keys()):
                for method, operation in sorted(paths[path].items()):
                    # Generate Python method
                    method_code = generate_method(
                        path, 
                        method, 
                        operation, 
                        openapi.get('components', {'schemas': {}})
                    )
                    f.write(method_code)
        
        # Create a subset OpenAPI schema
        openapi_subset = create_subset_openapi(
            tag,
            openapi['paths'],
            openapi.get('components', {}).get('schemas', {}),
            openapi['info']
        )
        
        # Write subset schema to file
        schema_file = os.path.join(output_dir, f"{tag.lower()}_openapi.json")
        with open(schema_file, 'w', encoding='utf-8') as f:
            json.dump(openapi_subset, f, indent=2)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Process an OpenAPI schema into separate tools")
    parser.add_argument("input_file", help="Path to the OpenAPI schema file")
    parser.add_argument("--output-dir", default="generated_tools", 
                       help="Directory to output generated tools (default: generated_tools)")
    args = parser.parse_args()
    
    process_openapi(args.input_file, args.output_dir)
    print(f"Generated tools and schemas in {args.output_dir}")

if __name__ == "__main__":
    main()
