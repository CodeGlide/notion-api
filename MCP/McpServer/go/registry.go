package main

import (
	"github.com/notion-api-public-beta/mcp-server/config"
	"github.com/notion-api-public-beta/mcp-server/models"
	tools_blocks "github.com/notion-api-public-beta/mcp-server/tools/blocks"
	tools_databases "github.com/notion-api-public-beta/mcp-server/tools/databases"
	tools_users "github.com/notion-api-public-beta/mcp-server/tools/users"
	tools_pages "github.com/notion-api-public-beta/mcp-server/tools/pages"
	tools_database "github.com/notion-api-public-beta/mcp-server/tools/database"
	tools_v1 "github.com/notion-api-public-beta/mcp-server/tools/v1"
)

func GetAll(cfg *config.APIConfig) []models.Tool {
	return []models.Tool{
		tools_blocks.CreateRetrieveblockchildrenTool(cfg),
		tools_blocks.CreateAppendblockchildrenTool(cfg),
		tools_databases.CreateQuerydatabaseTool(cfg),
		tools_databases.CreateRetrievedatabaseTool(cfg),
		tools_users.CreateRetrieveuserTool(cfg),
		tools_pages.CreateRetrievepageTool(cfg),
		tools_pages.CreateUpdatepagepropertiesTool(cfg),
		tools_users.CreateListallusersTool(cfg),
		tools_database.CreateListalldatabasesTool(cfg),
		tools_database.CreateCreatedatabaseTool(cfg),
		tools_pages.CreateCreatepageTool(cfg),
		tools_v1.CreateSearchpagesTool(cfg),
	}
}
