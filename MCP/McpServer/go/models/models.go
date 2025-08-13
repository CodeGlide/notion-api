package models

import (
	"context"
	"github.com/mark3labs/mcp-go/mcp"
)

type Tool struct {
	Definition mcp.Tool
	Handler    func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error)
}

// PageParent represents the PageParent schema from the OpenAPI specification
type PageParent struct {
	Database_id string `json:"database_id,omitempty"` // Database ID
}

// DatabaseProperties represents the DatabaseProperties schema from the OpenAPI specification
type DatabaseProperties struct {
	Files string `json:"files,omitempty"` // File database property schema object
	Last_edited_by string `json:"last_edited_by,omitempty"` // Last edited by database property schema object
	Number map[string]interface{} `json:"number,omitempty"` // Number database property schema object
	Phone_number string `json:"phone_number,omitempty"` // Phone number database property schema object
	SelectField SelectOptions `json:"select,omitempty"` // Select option
	Rich_text string `json:"rich_text,omitempty"` // Text database property schema objects
	Created_time string `json:"created_time,omitempty"` // Created time database property schema object
	Created_by string `json:"created_by,omitempty"` // Created by database property schema object
	Title string `json:"title,omitempty"` // Each database must have exactly one database property schema object of type "title". This database property controls the title that appears at the top of the page when the page is opened.
	Email string `json:"email,omitempty"` // Email database property schema object
	Multi_select []SelectOptions `json:"multi_select,omitempty"` // Multi-select database property schema object
	People string `json:"people,omitempty"` // People database property schema
	Date string `json:"date,omitempty"` // Date database property schema
	Last_edited_time string `json:"last_edited_time,omitempty"` // Last edited time database property schema object
	Checkbox string `json:"checkbox,omitempty"` // Checkbox database property schema object
	Url string `json:"url,omitempty"` // URL database property schema object
}

// PageResponse represents the PageResponse schema from the OpenAPI specification
type PageResponse struct {
	Object string `json:"object,omitempty"` // The object type "page"
	Parent map[string]interface{} `json:"parent,omitempty"` // Parent Page
	Properties ObjectProperties `json:"properties,omitempty"` // Object Properties
	Archived bool `json:"archived,omitempty"` // Indicates whether it is archived or not
	Created_time string `json:"created_time,omitempty"` // The created date/time
	Id string `json:"id,omitempty"` // ID of the page
	Last_edited_time string `json:"last_edited_time,omitempty"` // The last edited date/time
}

// Annotations represents the Annotations schema from the OpenAPI specification
type Annotations struct {
	Italic bool `json:"italic,omitempty"` // Whether the text is italic
	Strikethrough bool `json:"strikethrough,omitempty"` // Whether the text is struck through
	Underline bool `json:"underline,omitempty"` // Whether the text is underlined
	Bold bool `json:"bold,omitempty"` // Whether the text is bolded
	Code bool `json:"code,omitempty"` // Whether the text is "code style"
	Color string `json:"color,omitempty"` // Color of the text. Possible values are- "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", "blue_background", "purple_background", "pink_background", "red_background"
}

// Database represents the Database schema from the OpenAPI specification
type Database struct {
	Properties ObjectProperties `json:"properties,omitempty"` // Object Properties
	Title []map[string]interface{} `json:"title,omitempty"` // Title of the database
	Created_time string `json:"created_time,omitempty"` // The created date/time
	Id string `json:"id,omitempty"` // Database ID
	Last_edited_time string `json:"last_edited_time,omitempty"` // The last edited date/time
	Object string `json:"object,omitempty"` // Object type "database"
}

// ObjectProperties represents the ObjectProperties schema from the OpenAPI specification
type ObjectProperties struct {
	Author map[string]interface{} `json:"Author,omitempty"` // Author of the database
	Name map[string]interface{} `json:"Name,omitempty"` // The name of the object
	Publishing_release_date map[string]interface{} `json:"Publishing/Release Date,omitempty"` // Publishing/Releasing Date
	Read map[string]interface{} `json:"Read,omitempty"` // Read details
	Status map[string]interface{} `json:"Status,omitempty"` // The status ID
	Link map[string]interface{} `json:"Link,omitempty"` // Related links
	Summary map[string]interface{} `json:"Summary,omitempty"` // The summary of the database
	Publisher map[string]interface{} `json:"Publisher,omitempty"` // Publisher Detail
	TypeField map[string]interface{} `json:"Type,omitempty"` // The database type details
}

// SelectOptions represents the SelectOptions schema from the OpenAPI specification
type SelectOptions struct {
	Color string `json:"color,omitempty"` // Color of the option. Possible values include- default, gray, brown, orange, yellow, green, blue, purple, pink, red
	Name string `json:"name,omitempty"` // Name of the option as it appears in Notion
}

// PageUpdatedProperties represents the PageUpdatedProperties schema from the OpenAPI specification
type PageUpdatedProperties struct {
	Object string `json:"object,omitempty"` // The object type "page"
	Properties ObjectProperties `json:"properties,omitempty"` // Object Properties
	Archived bool `json:"archived,omitempty"` // Indicates whether it is archived or not
	Created_time string `json:"created_time,omitempty"` // The created date/time
	Id string `json:"id,omitempty"` // The ID of the Page
	Last_edited_time string `json:"last_edited_time,omitempty"` // The last edited date/time
}

// PaginatedDatabases represents the PaginatedDatabases schema from the OpenAPI specification
type PaginatedDatabases struct {
	Results []Database `json:"results,omitempty"` // Array of Users
	Has_more bool `json:"has_more,omitempty"` // Indicates whether there are more user records or not
	Next_cursor string `json:"next_cursor,omitempty"` // Next curser position of the user list
}

// ChildBlockContent represents the ChildBlockContent schema from the OpenAPI specification
type ChildBlockContent struct {
	TypeField string `json:"type,omitempty"` // Type of the block. Possible values include "paragraph", "heading_1", "heading_2", "heading_3", "bulleted_list_item" etc.
	Child_page map[string]interface{} `json:"child_page,omitempty"` // Child page
	Created_time string `json:"created_time,omitempty"` // The created date/time
	Has_children bool `json:"has_children,omitempty"` // Indicates whether it has children blocks
	Id string `json:"id,omitempty"` // ID of the block
	Last_edited_time string `json:"last_edited_time,omitempty"` // The last edited date/time
	Object string `json:"object,omitempty"` // Always "block" for block types
}

// PaginatedUsers represents the PaginatedUsers schema from the OpenAPI specification
type PaginatedUsers struct {
	Has_more bool `json:"has_more,omitempty"` // Indicates whether there are more user records or not
	Next_cursor string `json:"next_cursor,omitempty"` // Next curser position of the user list
	Results []User `json:"results,omitempty"` // Array of Users
}

// ResultDetails represents the ResultDetails schema from the OpenAPI specification
type ResultDetails struct {
	Last_edited_time string `json:"last_edited_time,omitempty"` // The last date/time
	Object string `json:"object,omitempty"` // Object Category
	TypeField string `json:"type,omitempty"` // object type
	Unsupported map[string]interface{} `json:"unsupported,omitempty"` // Unsupported
	Created_time string `json:"created_time,omitempty"` // The created date/time
	Has_children bool `json:"has_children,omitempty"` // Indicates whether it has child object or not
	Id string `json:"id,omitempty"` // Object ID
}

// DatabaseBodyParams represents the DatabaseBodyParams schema from the OpenAPI specification
type DatabaseBodyParams struct {
	Parent DatabaseParent `json:"parent,omitempty"` // Parent Page Detail
	Properties DatabaseProperties `json:"properties,omitempty"` // Property schema of database. The keys are the names of properties as they appear in Notion and the values are property schema objects
	Title []DatabaseTitle `json:"title,omitempty"` // Property schema of database
}

// DatabaseParent represents the DatabaseParent schema from the OpenAPI specification
type DatabaseParent struct {
	Page_id string `json:"page_id,omitempty"` // Database ID
}

// PageContent represents the PageContent schema from the OpenAPI specification
type PageContent struct {
	Properties map[string]interface{} `json:"properties,omitempty"` // Page properties
}

// SearchBody represents the SearchBody schema from the OpenAPI specification
type SearchBody struct {
	Filter Filtering `json:"filter,omitempty"` // When supplied, filters the results based on the provided criteria
	Page_size int `json:"page_size,omitempty"` // The number of items from the full list desired in the response. Maximum- 100
	Query string `json:"query,omitempty"` // When supplied, limits which pages are returned by comparing the query to the page title
	Sort Sorting `json:"sort,omitempty"` // When supplied, sorts the results based on the provided criteria
	Start_cursor string `json:"start_cursor,omitempty"` // If supplied, this endpoint will return a page of results starting after the cursor provided or else this endpoint will return the first page of results
}

// Sorting represents the Sorting schema from the OpenAPI specification
type Sorting struct {
	Direction string `json:"direction,omitempty"` // The direction to sort. Possible values include ascending and descending
	Timestamp string `json:"timestamp,omitempty"` // The name of the timestamp to sort against. Possible values include last_edited_time
}

// DatabaseResponse represents the DatabaseResponse schema from the OpenAPI specification
type DatabaseResponse struct {
	Has_more bool `json:"has_more,omitempty"` // Indicates whether has more objects
	Next_cursor interface{} `json:"next_cursor,omitempty"` // The next position of the result
	Object string `json:"object,omitempty"` // Object Type "list"
	Results []interface{} `json:"results,omitempty"` // Database results
}

// DatabaseTitle represents the DatabaseTitle schema from the OpenAPI specification
type DatabaseTitle struct {
	Annotation Annotations `json:"annotation,omitempty"` // Style information which applies to the whole rich text object
	Href string `json:"href,omitempty"` // The URL of any link or internal Notion mention in this text, if any
	Plain_text string `json:"plain_text,omitempty"` // The plain text without annotations
	TypeField string `json:"type,omitempty"` // Type of this rich text object. Possible values are- "text", "mention", "equation"
}

// BlockContent represents the BlockContent schema from the OpenAPI specification
type BlockContent struct {
	Text []map[string]interface{} `json:"text,omitempty"` // block objects
}

// User represents the User schema from the OpenAPI specification
type User struct {
	Id string `json:"id,omitempty"` // User ID
	Name string `json:"name,omitempty"` // Name of the User
	Object string `json:"object,omitempty"` // The object type User
	Person map[string]interface{} `json:"person,omitempty"` // The contact detail
	TypeField string `json:"type,omitempty"` // The object type
	Avatar_url interface{} `json:"avatar_url,omitempty"` // avatar URL
}

// PageBodyParams represents the PageBodyParams schema from the OpenAPI specification
type PageBodyParams struct {
	Properties PageProperties `json:"properties,omitempty"` // Page properties
	Children []map[string]interface{} `json:"children,omitempty"` // Page content for the new page
	Parent PageParent `json:"parent,omitempty"` // Parent Page Detail
}

// BlockChildrenResponse represents the BlockChildrenResponse schema from the OpenAPI specification
type BlockChildrenResponse struct {
	Has_more bool `json:"has_more,omitempty"` // Indicates whether it has more objects or not
	Next_cursor interface{} `json:"next_cursor,omitempty"` // Incidates the position of the response list
	Object string `json:"object,omitempty"` // The response object
	Results []ResultDetails `json:"results,omitempty"` // The array of result details
}

// PageProperties represents the PageProperties schema from the OpenAPI specification
type PageProperties struct {
	Name string `json:"name,omitempty"` // The ID of the property
	TypeField string `json:"type,omitempty"` // Type of the property
}

// PageUpdateRequestBody represents the PageUpdateRequestBody schema from the OpenAPI specification
type PageUpdateRequestBody struct {
	Children []map[string]interface{} `json:"children,omitempty"` // Children pages
}

// Filtering represents the Filtering schema from the OpenAPI specification
type Filtering struct {
	Property string `json:"property,omitempty"` // The name of the property to filter by.
	Value string `json:"value,omitempty"` // The value of the property to filter the results by and Possible values for object type include page or database
}

// DatabaseContent represents the DatabaseContent schema from the OpenAPI specification
type DatabaseContent struct {
	Sorts []map[string]interface{} `json:"sorts,omitempty"` // Sorting details
	Filter map[string]interface{} `json:"filter,omitempty"` // Filter detail
}
