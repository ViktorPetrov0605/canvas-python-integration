#!/usr/bin/env python3
"""
Test Script for OpenAPI Parser and Proxy

This script:
1. Parses the test OpenAPI schema
2. Generates tool classes for each tag
3. Demonstrates usage of the generated tools
"""

import os
import json
import subprocess
import argparse
from pathlib import Path

def run_parser(openapi_file, output_dir):
    """Run the OpenAPI parser on the given file."""
    print(f"Parsing OpenAPI schema: {openapi_file}")
    
    # Ensure the parser script exists
    if not os.path.exists("openapi_parser.py"):
        print("Error: openapi_parser.py not found")
        return False
    
    # Run the parser
    cmd = ["python3", "openapi_parser.py", openapi_file, "--output-dir", output_dir]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running parser: {result.stderr}")
        return False
    
    print(result.stdout)
    return True

def test_proxy(openapi_file, tag):
    """Test starting the OpenAPI proxy for a specific tag."""
    print(f"Testing OpenAPI proxy for tag: {tag}")
    
    # Ensure the proxy script exists
    if not os.path.exists("openapi_proxy.py"):
        print("Error: openapi_proxy.py not found")
        return False
    
    # Command to start the proxy (we won't actually run it here)
    cmd = [
        "python3", "openapi_proxy.py",
        "--openapi", openapi_file,
        "--target", "http://localhost:8000",
        "--host", "127.0.0.1",
        "--port", "7899",
        "--tags", tag
    ]
    
    print("\nTo start the proxy, run:")
    print(" ".join(cmd))
    print("\nThe proxy will serve only the endpoints tagged with:", tag)
    print("You can access the OpenAPI schema at: http://127.0.0.1:7899/openapi.json")
    
    return True

def show_example_usage(output_dir, tag):
    """Show example usage of the generated tool class."""
    tool_file = os.path.join(output_dir, f"{tag}_tool.py")
    
    if not os.path.exists(tool_file):
        print(f"Error: Generated tool file not found: {tool_file}")
        return False
    
    print(f"\nExample usage of {tag.capitalize()} API Tool:")
    print(f"-------------------------------------------")
    print(f"```python")
    print(f"from {tag}_tool import Tools")
    print(f"")
    print(f"# Initialize the API client")
    print(f"client = Tools()")
    print(f"")
    print(f"# Set environment variables for configuration")
    print(f"import os")
    print(f"os.environ['API_BASE_URL'] = 'http://localhost:8000'")
    print(f"os.environ['API_KEY'] = 'your_api_key_here'  # if required")
    print(f"")
    
    # Read the generated file to extract method names
    with open(tool_file, 'r') as f:
        content = f.read()
    
    # Find method names using a simple pattern
    import re
    methods = re.findall(r'def\s+(\w+)\s*\(self,', content)
    
    if methods:
        print(f"# Examples of available methods:")
        for method in methods[:3]:  # Show first 3 methods
            print(f"response = client.{method}()")
            print(f"print(response)")
            print()
    
    print(f"```")
    return True

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Test OpenAPI Parser and Proxy")
    parser.add_argument("--openapi", default="test_openapi.json", 
                        help="Path to OpenAPI schema file (default: test_openapi.json)")
    parser.add_argument("--output-dir", default="generated_tools",
                        help="Directory for generated tools (default: generated_tools)")
    parser.add_argument("--tag", default="users",
                        help="Tag to use for testing (default: users)")
    args = parser.parse_args()
    
    # Run the parser
    if not run_parser(args.openapi, args.output_dir):
        return
    
    # Show example usage
    show_example_usage(args.output_dir, args.tag)
    
    # Test proxy
    test_proxy(args.openapi, args.tag)
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
