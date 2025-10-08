"""Data models for notion_api_public_beta."""
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SearchBody(BaseModel):
    """SearchBody schema from the OpenAPI specification."""
    query: str = Field(alias="query")  # When supplied, limits which pages are returned by comparing the query to the page title
    sort: Sorting = Field(alias="sort")  # When supplied, sorts the results based on the provided criteria
    filter: Filtering = Field(alias="filter")  # When supplied, filters the results based on the provided criteria
    start_cursor: str = Field(alias="start_cursor")  # If supplied, this endpoint will return a page of results starting after the cursor provided or else this endpoint will return the first page of results
    page_size: int = Field(alias="page_size")  # The number of items from the full list desired in the response. Maximum- 100
    
    class Config:
        populate_by_name = True


class Sorting(BaseModel):
    """Sorting schema from the OpenAPI specification."""
    direction: str = Field(alias="direction")  # The direction to sort. Possible values include ascending and descending
    timestamp: str = Field(alias="timestamp")  # The name of the timestamp to sort against. Possible values include last_edited_time
    
    class Config:
        populate_by_name = True


class Filtering(BaseModel):
    """Filtering schema from the OpenAPI specification."""
    value: str = Field(alias="value")  # The value of the property to filter the results by and Possible values for object type include page or database
    property: str = Field(alias="property")  # The name of the property to filter by.
    
    class Config:
        populate_by_name = True


class PaginatedUsers(BaseModel):
    """PaginatedUsers schema from the OpenAPI specification."""
    results: List[User] = Field(alias="results")  # Array of Users
    next_cursor: str = Field(alias="next_cursor")  # Next curser position of the user list
    has_more: bool = Field(alias="has_more")  # Indicates whether there are more user records or not
    
    class Config:
        populate_by_name = True


class PageUpdateRequestBody(BaseModel):
    """PageUpdateRequestBody schema from the OpenAPI specification."""
    children: List[Dict[str, Any]] = Field(alias="children")  # Children pages
    
    class Config:
        populate_by_name = True


class PaginatedDatabases(BaseModel):
    """PaginatedDatabases schema from the OpenAPI specification."""
    results: List[Database] = Field(alias="results")  # Array of Users
    next_cursor: str = Field(alias="next_cursor")  # Next curser position of the user list
    has_more: bool = Field(alias="has_more")  # Indicates whether there are more user records or not
    
    class Config:
        populate_by_name = True


class ObjectProperties(BaseModel):
    """ObjectProperties schema from the OpenAPI specification."""
    author: Dict[str, Any] = Field(alias="Author")  # Author of the database
    link: Dict[str, Any] = Field(alias="Link")  # Related links
    name: Dict[str, Any] = Field(alias="Name")  # The name of the object
    publisher: Dict[str, Any] = Field(alias="Publisher")  # Publisher Detail
    publishing_release_date: Dict[str, Any] = Field(alias="Publishing/Release Date")  # Publishing/Releasing Date
    read: Dict[str, Any] = Field(alias="Read")  # Read details
    status: Dict[str, Any] = Field(alias="Status")  # The status ID
    summary: Dict[str, Any] = Field(alias="Summary")  # The summary of the database
    type_field: Dict[str, Any] = Field(alias="Type")  # The database type details
    
    class Config:
        populate_by_name = True


class ResultDetails(BaseModel):
    """ResultDetails schema from the OpenAPI specification."""
    created_time: str = Field(alias="created_time")  # The created date/time
    has_children: bool = Field(alias="has_children")  # Indicates whether it has child object or not
    id_field: str = Field(alias="id")  # Object ID
    last_edited_time: str = Field(alias="last_edited_time")  # The last date/time
    object_field: str = Field(alias="object")  # Object Category
    type_field: str = Field(alias="type")  # object type
    unsupported: Dict[str, Any] = Field(alias="unsupported")  # Unsupported
    
    class Config:
        populate_by_name = True


class BlockChildrenResponse(BaseModel):
    """BlockChildrenResponse schema from the OpenAPI specification."""
    has_more: bool = Field(alias="has_more")  # Indicates whether it has more objects or not
    next_cursor: Any = Field(alias="next_cursor")  # Incidates the position of the response list
    object_field: str = Field(alias="object")  # The response object
    results: List[ResultDetails] = Field(alias="results")  # The array of result details
    
    class Config:
        populate_by_name = True


class ChildBlockContent(BaseModel):
    """ChildBlockContent schema from the OpenAPI specification."""
    child_page: Dict[str, Any] = Field(alias="child_page")  # Child page
    created_time: str = Field(alias="created_time")  # The created date/time
    has_children: bool = Field(alias="has_children")  # Indicates whether it has children blocks
    id_field: str = Field(alias="id")  # ID of the block
    last_edited_time: str = Field(alias="last_edited_time")  # The last edited date/time
    object_field: str = Field(alias="object")  # Always \"block\" for block types
    type_field: str = Field(alias="type")  # Type of the block. Possible values include \"paragraph\", \"heading_1\", \"heading_2\", \"heading_3\", \"bulleted_list_item\" etc.
    
    class Config:
        populate_by_name = True


class Database(BaseModel):
    """Database schema from the OpenAPI specification."""
    created_time: str = Field(alias="created_time")  # The created date/time
    id_field: str = Field(alias="id")  # Database ID
    last_edited_time: str = Field(alias="last_edited_time")  # The last edited date/time
    object_field: str = Field(alias="object")  # Object type \"database\"
    properties: ObjectProperties = Field(alias="properties")  # Object Properties
    title: List[Dict[str, Any]] = Field(alias="title")  # Title of the database
    
    class Config:
        populate_by_name = True


class DatabaseContent(BaseModel):
    """DatabaseContent schema from the OpenAPI specification."""
    filter: Dict[str, Any] = Field(alias="filter")  # Filter detail
    sorts: List[Dict[str, Any]] = Field(alias="sorts")  # Sorting details
    
    class Config:
        populate_by_name = True


class DatabaseResponse(BaseModel):
    """DatabaseResponse schema from the OpenAPI specification."""
    has_more: bool = Field(alias="has_more")  # Indicates whether has more objects
    next_cursor: Any = Field(alias="next_cursor")  # The next position of the result
    object_field: str = Field(alias="object")  # Object Type \"list\"
    results: List[Any] = Field(alias="results")  # Database results
    
    class Config:
        populate_by_name = True


class PageResponse(BaseModel):
    """PageResponse schema from the OpenAPI specification."""
    archived: bool = Field(alias="archived")  # Indicates whether it is archived or not
    created_time: str = Field(alias="created_time")  # The created date/time
    id_field: str = Field(alias="id")  # ID of the page
    last_edited_time: str = Field(alias="last_edited_time")  # The last edited date/time
    object_field: str = Field(alias="object")  # The object type \"page\"
    parent: Dict[str, Any] = Field(alias="parent")  # Parent Page
    properties: ObjectProperties = Field(alias="properties")  # Object Properties
    
    class Config:
        populate_by_name = True


class PageContent(BaseModel):
    """PageContent schema from the OpenAPI specification."""
    properties: Dict[str, Any] = Field(alias="properties")  # Page properties
    
    class Config:
        populate_by_name = True


class PageUpdatedProperties(BaseModel):
    """PageUpdatedProperties schema from the OpenAPI specification."""
    archived: bool = Field(alias="archived")  # Indicates whether it is archived or not
    created_time: str = Field(alias="created_time")  # The created date/time
    id_field: str = Field(alias="id")  # The ID of the Page
    last_edited_time: str = Field(alias="last_edited_time")  # The last edited date/time
    object_field: str = Field(alias="object")  # The object type \"page\"
    properties: ObjectProperties = Field(alias="properties")  # Object Properties
    
    class Config:
        populate_by_name = True


class User(BaseModel):
    """User schema from the OpenAPI specification."""
    avatar_url: Any = Field(alias="avatar_url")  # avatar URL
    id_field: str = Field(alias="id")  # User ID
    name: str = Field(alias="name")  # Name of the User
    object_field: str = Field(alias="object")  # The object type User
    person: Dict[str, Any] = Field(alias="person")  # The contact detail
    type_field: str = Field(alias="type")  # The object type
    
    class Config:
        populate_by_name = True


class PageProperties(BaseModel):
    """PageProperties schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The ID of the property
    type_field: str = Field(alias="type")  # Type of the property
    
    class Config:
        populate_by_name = True


class DatabaseTitle(BaseModel):
    """DatabaseTitle schema from the OpenAPI specification."""
    plain_text: str = Field(alias="plain_text")  # The plain text without annotations
    href: str = Field(alias="href")  # The URL of any link or internal Notion mention in this text, if any
    type_field: str = Field(alias="type")  # Type of this rich text object. Possible values are- \"text\", \"mention\", \"equation\"
    annotation: Annotations = Field(alias="annotation")  # Style information which applies to the whole rich text object
    
    class Config:
        populate_by_name = True


class Annotations(BaseModel):
    """Annotations schema from the OpenAPI specification."""
    bold: bool = Field(alias="bold")  # Whether the text is bolded
    italic: bool = Field(alias="italic")  # Whether the text is italic
    strikethrough: bool = Field(alias="strikethrough")  # Whether the text is struck through
    underline: bool = Field(alias="underline")  # Whether the text is underlined
    code: bool = Field(alias="code")  # Whether the text is \"code style\"
    color: str = Field(alias="color")  # Color of the text. Possible values are- \"default\", \"gray\", \"brown\", \"orange\", \"yellow\", \"green\", \"blue\", \"purple\", \"pink\", \"red\", \"gray_background\", \"brown_background\", \"orange_background\", \"yellow_background\", \"green_background\", \"blue_background\", \"purple_background\", \"pink_background\", \"red_background\"
    
    class Config:
        populate_by_name = True


class PageParent(BaseModel):
    """PageParent schema from the OpenAPI specification."""
    database_id: str = Field(alias="database_id")  # Database ID
    
    class Config:
        populate_by_name = True


class DatabaseParent(BaseModel):
    """DatabaseParent schema from the OpenAPI specification."""
    page_id: str = Field(alias="page_id")  # Database ID
    
    class Config:
        populate_by_name = True


class PageBodyParams(BaseModel):
    """PageBodyParams schema from the OpenAPI specification."""
    properties: PageProperties = Field(alias="properties")  # Page properties
    parent: PageParent = Field(alias="parent")  # Parent Page Detail
    children: List[Dict[str, Any]] = Field(alias="children")  # Page content for the new page
    
    class Config:
        populate_by_name = True


class DatabaseBodyParams(BaseModel):
    """DatabaseBodyParams schema from the OpenAPI specification."""
    properties: DatabaseProperties = Field(alias="properties")  # Property schema of database. The keys are the names of properties as they appear in Notion and the values are property schema objects
    parent: DatabaseParent = Field(alias="parent")  # Parent Page Detail
    title: List[DatabaseTitle] = Field(alias="title")  # Property schema of database
    
    class Config:
        populate_by_name = True


class DatabaseProperties(BaseModel):
    """DatabaseProperties schema from the OpenAPI specification."""
    title: str = Field(alias="title")  # Each database must have exactly one database property schema object of type \"title\". This database property controls the title that appears at the top of the page when the page is opened.
    rich_text: str = Field(alias="rich_text")  # Text database property schema objects
    number: Dict[str, Any] = Field(alias="number")  # Number database property schema object
    select: SelectOptions = Field(alias="select")  # Select option
    multi_select: List[SelectOptions] = Field(alias="multi_select")  # Multi-select database property schema object
    date: str = Field(alias="date")  # Date database property schema
    people: str = Field(alias="people")  # People database property schema
    files: str = Field(alias="files")  # File database property schema object
    checkbox: str = Field(alias="checkbox")  # Checkbox database property schema object
    url: str = Field(alias="url")  # URL database property schema object
    email: str = Field(alias="email")  # Email database property schema object
    phone_number: str = Field(alias="phone_number")  # Phone number database property schema object
    last_edited_time: str = Field(alias="last_edited_time")  # Last edited time database property schema object
    last_edited_by: str = Field(alias="last_edited_by")  # Last edited by database property schema object
    created_time: str = Field(alias="created_time")  # Created time database property schema object
    created_by: str = Field(alias="created_by")  # Created by database property schema object
    
    class Config:
        populate_by_name = True


class SelectOptions(BaseModel):
    """SelectOptions schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # Name of the option as it appears in Notion
    color: str = Field(alias="color")  # Color of the option. Possible values include- default, gray, brown, orange, yellow, green, blue, purple, pink, red
    
    class Config:
        populate_by_name = True


class BlockContent(BaseModel):
    """BlockContent schema from the OpenAPI specification."""
    text: List[Dict[str, Any]] = Field(alias="text")  # block objects
    
    class Config:
        populate_by_name = True