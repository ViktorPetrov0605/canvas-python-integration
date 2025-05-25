"""
title: Items API Tool
author: Auto Generated
description: API Tool for interacting with Items endpoints
required_open_webui_version: 0.5.0
requirements: requests
version: 0.1.0
licence: MIT
"""

import os
import requests
from typing import Dict, Any, List, Optional, Union


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

    def list_items(self, limit: Optional[int] = None) -> dict:
        """
        List Items
        
        No description provided
        
        :param limit: Maximum number of items to return
        :return: Dictionary with API response data or error details
        """
        url = self.api_base + "/items"
        
        # No payload required
        params = {
            "limit": limit,
        }
        
        try:
            method = "get".lower()
            if method == "get":
                response = requests.get(url, params=params, headers=self.headers)
            elif method == "post":
                response = requests.post(url, params=params, headers=self.headers)
            elif method == "put":
                response = requests.put(url, params=params, headers=self.headers)
            elif method == "delete":
                response = requests.delete(url, params=params, headers=self.headers)
            elif method == "patch":
                response = requests.patch(url, params=params, headers=self.headers)
            else:
                response = requests.get(url, params=params, headers=self.headers)
            
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "error": str(e),
                "status_code": getattr(response, "status_code", None),
                "text": getattr(response, "text", ""),
            }
