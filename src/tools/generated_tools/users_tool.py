"""
title: Users API Tool
author: Auto Generated
description: API Tool for interacting with Users endpoints
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

    def delete_user(self, user_id: int) -> dict:
        """
        Delete User
        
        No description provided
        
        :param user_id: ID of the user to delete
        :return: Dictionary with API response data or error details
        """
        url = self.api_base + f"/users/{user_id}"
        
        # No payload required
        
        try:
            method = "delete".lower()
            if method == "get":
                response = requests.get(url, headers=self.headers)
            elif method == "post":
                response = requests.post(url, headers=self.headers)
            elif method == "put":
                response = requests.put(url, headers=self.headers)
            elif method == "delete":
                response = requests.delete(url, headers=self.headers)
            elif method == "patch":
                response = requests.patch(url, headers=self.headers)
            else:
                response = requests.get(url, headers=self.headers)
            
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "error": str(e),
                "status_code": getattr(response, "status_code", None),
                "text": getattr(response, "text", ""),
            }

    def get_user(self, user_id: int) -> dict:
        """
        Get User by ID
        
        No description provided
        
        :param user_id: ID of the user to get
        :return: Dictionary with API response data or error details
        """
        url = self.api_base + f"/users/{user_id}"
        
        # No payload required
        
        try:
            method = "get".lower()
            if method == "get":
                response = requests.get(url, headers=self.headers)
            elif method == "post":
                response = requests.post(url, headers=self.headers)
            elif method == "put":
                response = requests.put(url, headers=self.headers)
            elif method == "delete":
                response = requests.delete(url, headers=self.headers)
            elif method == "patch":
                response = requests.patch(url, headers=self.headers)
            else:
                response = requests.get(url, headers=self.headers)
            
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {
                "error": str(e),
                "status_code": getattr(response, "status_code", None),
                "text": getattr(response, "text", ""),
            }
