#!/usr/bin/env python3
"""
OpenAPI Proxy Server

This script creates a FastAPI server that:
1. Serves a subset of an OpenAPI schema
2. Proxies requests to the real API server
3. Forwards authentication headers
"""

import argparse
import json
import os
import httpx
from typing import Any, Dict, List, Optional, Union
from fastapi import FastAPI, Request, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_cors_middleware(
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global config
config = {
    "target_url": "http://localhost:8000",
    "openapi_path": "./openapi.json",
    "proxy_prefix": "",
    "include_tags": []
}

# HTTP client for proxying requests
client = httpx.AsyncClient()

# Function to load and filter OpenAPI schema
def load_openapi_schema(
    openapi_path: str,
    include_tags: List[str] = None,
    proxy_prefix: str = ""
) -> Dict[str, Any]:
    """Load an OpenAPI schema and filter it based on tags."""
    with open(openapi_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    
    # If no tags specified, return the full schema
    if not include_tags:
        return schema
    
    # Create a new schema with only the requested tags
    filtered_schema = {
        "openapi": schema["openapi"],
        "info": schema["info"],
        "paths": {},
        "components": schema.get("components", {})
    }
    
    # Filter paths by tag
    for path, methods in schema["paths"].items():
        for method, operation in methods.items():
            tags = operation.get("tags", [])
            if any(tag in include_tags for tag in tags):
                if path not in filtered_schema["paths"]:
                    filtered_schema["paths"][path] = {}
                filtered_schema["paths"][path][method] = operation
    
    # Update paths with proxy prefix if provided
    if proxy_prefix:
        prefixed_paths = {}
        for path, methods in filtered_schema["paths"].items():
            prefixed_path = f"{proxy_prefix}{path}"
            prefixed_paths[prefixed_path] = methods
        filtered_schema["paths"] = prefixed_paths
    
    return filtered_schema

@app.get("/openapi.json")
async def get_openapi():
    """Serve the filtered OpenAPI schema."""
    try:
        schema = load_openapi_schema(
            config["openapi_path"],
            config["include_tags"],
            config["proxy_prefix"]
        )
        return JSONResponse(content=schema)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading OpenAPI schema: {str(e)}")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def proxy_endpoint(request: Request, path: str, authorization: Optional[str] = Header(None)):
    """Proxy all requests to the target server."""
    # Build target URL
    target_url = f"{config['target_url']}/{path}"
    
    # Get request body if any
    body = None
    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.body()
    
    # Prepare headers
    headers = dict(request.headers)
    if "host" in headers:
        del headers["host"]  # Remove host header to avoid conflicts
    
    # Get query parameters
    params = dict(request.query_params)
    
    try:
        # Make the request to the target server
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=params,
            content=body
        )
        
        # Return the proxied response
        return JSONResponse(
            content=response.json() if response.headers.get("content-type") == "application/json" else response.text,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error proxying request: {str(e)}")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="OpenAPI Proxy Server")
    parser.add_argument("--openapi", default="./openapi.json", 
                        help="Path to OpenAPI schema file (default: ./openapi.json)")
    parser.add_argument("--target", default="http://localhost:8000",
                        help="Target URL to proxy requests to (default: http://localhost:8000)")
    parser.add_argument("--host", default="127.0.0.1",
                        help="Host to bind the server (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=7899,
                        help="Port to bind the server (default: 7899)")
    parser.add_argument("--tags", nargs="+", default=[],
                        help="Tags to include in the filtered OpenAPI schema")
    parser.add_argument("--prefix", default="",
                        help="Prefix to add to paths in the OpenAPI schema")
    args = parser.parse_args()
    
    # Update global config
    config.update({
        "target_url": args.target,
        "openapi_path": args.openapi,
        "proxy_prefix": args.prefix,
        "include_tags": args.tags
    })
    
    # Print configuration
    print(f"Starting OpenAPI Proxy Server:")
    print(f"  - Listening on: http://{args.host}:{args.port}")
    print(f"  - Proxying to: {args.target}")
    print(f"  - OpenAPI Schema: {args.openapi}")
    print(f"  - Included Tags: {args.tags if args.tags else 'All'}")
    print(f"  - Path Prefix: {args.prefix if args.prefix else 'None'}")
    
    # Start server with uvicorn
    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)

if __name__ == "__main__":
    main()
