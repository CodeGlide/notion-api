"""UpdatePageProperties tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatepageproperties(
    properties: dict = None
) -> str:
    """
    Update Page properties 
    
    Args:
        properties: Input parameter: Page properties
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Build request body
    request_body = {}
    if properties is not None:
        request_body["properties"] = properties
    
    # Build URL
    url = f"{config['base_url']}/v1/pages/{id}"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
    headers["Content-Type"] = "application/json"
    # Set authentication
    if config.get("bearer_token"):
        headers["Authorization"] = f"Bearer {config['bearer_token']}"
    
    # Add custom headers
    
    try:
        # Make API request
        response = requests.request(
            method="PATCH",
            url=url,
            headers=headers,
            json=request_body,
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