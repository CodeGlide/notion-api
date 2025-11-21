"""RetrieveBlockChildren tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def retrieveblockchildren(
    page_size: str = None,
    Notion_Version: str = None
) -> str:
    """
    Retrieve block children
    
    Args:
        page_size: Page size
        Notion_Version: API Version
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Build query parameters
    query_params = {}
    if page_size is not None:
        query_params["page_size"] = page_size
    
    # Build URL
    url = f"{config['base_url']}/v1/blocks/{id}/children"
    
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