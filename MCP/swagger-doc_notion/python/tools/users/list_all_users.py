"""ListAllUsers tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def listallusers(
    start_cursor: str = None,
    page_size: int = None,
    Notion_Version: str = None
) -> str:
    """
    List all users
    
    Args:
        start_cursor: If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
        page_size: The number of items from the full list desired in the response. Maximum- 100
        Notion_Version: API Version
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Build query parameters
    query_params = {}
    if start_cursor is not None:
        query_params["start_cursor"] = start_cursor
    if page_size is not None:
        query_params["page_size"] = page_size
    
    # Build URL
    url = f"{config['base_url']}/v1/users"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
    # Set authentication
    if config.get("bearer_token"):
        headers["Authorization"] = f"Bearer {config['bearer_token']}"
    
    # Add custom headers
    if Notion_Version is not None:
        headers["Notion-Version"] = str(Notion_Version)
    
    try:
        # Make API request
        response = requests.request(
            method="GET",
            url=url,
            params=query_params,
            headers=headers,
            timeout=30
        )
        
        if response.status_code >= 400:
            return json.dumps({
                "error": f"API error ({response.status_code})",
                "message": response.text
            })
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return response.text
            
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return json.dumps({"error": f"Request failed: {str(e)}"})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return json.dumps({"error": f"Error: {str(e)}"})