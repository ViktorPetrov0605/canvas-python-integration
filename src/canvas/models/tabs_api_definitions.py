from enum import Enum
from typing import Optional, List, Any


class Items:
    type: str

    def __init__(self, type: str) -> None:
        self.type = type


class ParamType(Enum):
    FORM = "form"
    PATH = "path"
    QUERY = "query"


class Parameter:
    param_type: ParamType
    name: str
    description: str
    type: str
    format: Optional[str]
    required: bool
    deprecated: bool
    enum: Optional[List[str]]
    items: Optional[Items]

    def __init__(self, param_type: ParamType, name: str, description: str, type: str, format: Optional[str], required: bool, deprecated: bool, enum: Optional[List[str]], items: Optional[Items]) -> None:
        self.param_type = param_type
        self.name = name
        self.description = description
        self.type = type
        self.format = format
        self.required = required
        self.deprecated = deprecated
        self.enum = enum
        self.items = items


class Operation:
    method: str
    summary: str
    notes: str
    nickname: str
    parameters: List[Parameter]
    response_fields: List[Any]
    deprecated: bool
    deprecation_description: str
    type: str

    def __init__(self, method: str, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[Any], deprecated: bool, deprecation_description: str, type: str) -> None:
        self.method = method
        self.summary = summary
        self.notes = notes
        self.nickname = nickname
        self.parameters = parameters
        self.response_fields = response_fields
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.type = type


class API:
    path: str
    description: str
    operations: List[Operation]

    def __init__(self, path: str, description: str, operations: List[Operation]) -> None:
        self.path = path
        self.description = description
        self.operations = operations


class Hidden:
    description: str
    example: bool
    type: str

    def __init__(self, description: str, example: bool, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class HTMLURL:
    example: str
    type: str

    def __init__(self, example: str, type: str) -> None:
        self.example = example
        self.type = type


class Position:
    description: str
    example: int
    type: str

    def __init__(self, description: str, example: int, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class Visibility:
    description: str
    example: str
    type: str

    def __init__(self, description: str, example: str, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class Properties:
    html_url: HTMLURL
    id: HTMLURL
    label: HTMLURL
    type: HTMLURL
    hidden: Hidden
    visibility: Visibility
    position: Position

    def __init__(self, html_url: HTMLURL, id: HTMLURL, label: HTMLURL, type: HTMLURL, hidden: Hidden, visibility: Visibility, position: Position) -> None:
        self.html_url = html_url
        self.id = id
        self.label = label
        self.type = type
        self.hidden = hidden
        self.visibility = visibility
        self.position = position


class Tab:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: Properties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: Properties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    tab: Tab

    def __init__(self, tab: Tab) -> None:
        self.tab = tab


class Welcome8:
    api_version: str
    swagger_version: str
    base_path: str
    resource_path: str
    produces: List[str]
    apis: List[API]
    models: Models

    def __init__(self, api_version: str, swagger_version: str, base_path: str, resource_path: str, produces: List[str], apis: List[API], models: Models) -> None:
        self.api_version = api_version
        self.swagger_version = swagger_version
        self.base_path = base_path
        self.resource_path = resource_path
        self.produces = produces
        self.apis = apis
        self.models = models
