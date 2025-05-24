from enum import Enum
from typing import Optional, List, Any


class RefEnum(Enum):
    FILE = "File"
    FOLDER = "Folder"
    LICENSE = "License"
    LOCK_INFO = "LockInfo"


class LockInfo:
    ref: RefEnum

    def __init__(self, ref: RefEnum) -> None:
        self.ref = ref


class Method(Enum):
    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class Format(Enum):
    INT64 = "int64"


class ItemsType(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    DATE_TIME = "DateTime"
    INTEGER = "integer"
    STRING = "string"


class Items:
    type: Optional[ItemsType]
    ref: Optional[str]

    def __init__(self, type: Optional[ItemsType], ref: Optional[str]) -> None:
        self.type = type
        self.ref = ref


class ParamType(Enum):
    FORM = "form"
    PATH = "path"
    QUERY = "query"


class Parameter:
    param_type: ParamType
    name: str
    description: str
    type: ItemsType
    format: Optional[Format]
    required: bool
    deprecated: bool
    items: Optional[Items]
    enum: Optional[List[str]]

    def __init__(self, param_type: ParamType, name: str, description: str, type: ItemsType, format: Optional[Format], required: bool, deprecated: bool, items: Optional[Items], enum: Optional[List[str]]) -> None:
        self.param_type = param_type
        self.name = name
        self.description = description
        self.type = type
        self.format = format
        self.required = required
        self.deprecated = deprecated
        self.items = items
        self.enum = enum


class TypeEnum(Enum):
    ARRAY = "array"
    FILE = "File"
    FOLDER = "Folder"
    USAGE_RIGHTS = "UsageRights"
    VOID = "void"


class Operation:
    method: Method
    summary: str
    notes: str
    nickname: str
    parameters: List[Parameter]
    response_fields: List[Any]
    deprecated: bool
    deprecation_description: str
    type: TypeEnum
    items: Optional[LockInfo]

    def __init__(self, method: Method, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[Any], deprecated: bool, deprecation_description: str, type: TypeEnum, items: Optional[LockInfo]) -> None:
        self.method = method
        self.summary = summary
        self.notes = notes
        self.nickname = nickname
        self.parameters = parameters
        self.response_fields = response_fields
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.type = type
        self.items = items


class API:
    path: str
    description: str
    operations: List[Operation]

    def __init__(self, path: str, description: str, operations: List[Operation]) -> None:
        self.path = path
        self.description = description
        self.operations = operations


class ContentTypeType(Enum):
    DATETIME = "datetime"
    STRING = "string"


class ContentType:
    example: str
    type: ContentTypeType

    def __init__(self, example: str, type: ContentTypeType) -> None:
        self.example = example
        self.type = type


class FolderID:
    example: int
    type: ItemsType

    def __init__(self, example: int, type: ItemsType) -> None:
        self.example = example
        self.type = type


class Hidden:
    example: bool
    type: ItemsType

    def __init__(self, example: bool, type: ItemsType) -> None:
        self.example = example
        self.type = type


class MediaEntryID:
    type: ItemsType
    example: str
    description: str

    def __init__(self, type: ItemsType, example: str, description: str) -> None:
        self.type = type
        self.example = example
        self.description = description


class PreviewURL:
    type: ItemsType
    description: str

    def __init__(self, type: ItemsType, description: str) -> None:
        self.type = type
        self.description = description


class Size:
    example: int
    type: ItemsType
    description: str

    def __init__(self, example: int, type: ItemsType, description: str) -> None:
        self.example = example
        self.type = type
        self.description = description


class ThumbnailURL:
    type: str

    def __init__(self, type: str) -> None:
        self.type = type


class FileProperties:
    id: FolderID
    uuid: ContentType
    folder_id: FolderID
    display_name: ContentType
    filename: ContentType
    content_type: ContentType
    url: ContentType
    size: Size
    created_at: ContentType
    updated_at: ContentType
    unlock_at: ContentType
    locked: Hidden
    hidden: Hidden
    lock_at: ContentType
    hidden_for_user: Hidden
    visibility_level: MediaEntryID
    thumbnail_url: ThumbnailURL
    modified_at: ContentType
    mime_class: MediaEntryID
    media_entry_id: MediaEntryID
    locked_for_user: Hidden
    lock_info: LockInfo
    lock_explanation: ContentType
    preview_url: PreviewURL

    def __init__(self, id: FolderID, uuid: ContentType, folder_id: FolderID, display_name: ContentType, filename: ContentType, content_type: ContentType, url: ContentType, size: Size, created_at: ContentType, updated_at: ContentType, unlock_at: ContentType, locked: Hidden, hidden: Hidden, lock_at: ContentType, hidden_for_user: Hidden, visibility_level: MediaEntryID, thumbnail_url: ThumbnailURL, modified_at: ContentType, mime_class: MediaEntryID, media_entry_id: MediaEntryID, locked_for_user: Hidden, lock_info: LockInfo, lock_explanation: ContentType, preview_url: PreviewURL) -> None:
        self.id = id
        self.uuid = uuid
        self.folder_id = folder_id
        self.display_name = display_name
        self.filename = filename
        self.content_type = content_type
        self.url = url
        self.size = size
        self.created_at = created_at
        self.updated_at = updated_at
        self.unlock_at = unlock_at
        self.locked = locked
        self.hidden = hidden
        self.lock_at = lock_at
        self.hidden_for_user = hidden_for_user
        self.visibility_level = visibility_level
        self.thumbnail_url = thumbnail_url
        self.modified_at = modified_at
        self.mime_class = mime_class
        self.media_entry_id = media_entry_id
        self.locked_for_user = locked_for_user
        self.lock_info = lock_info
        self.lock_explanation = lock_explanation
        self.preview_url = preview_url


class File:
    id: RefEnum
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: FileProperties

    def __init__(self, id: RefEnum, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: FileProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class ForSubmissions:
    example: bool
    type: ItemsType
    description: str

    def __init__(self, example: bool, type: ItemsType, description: str) -> None:
        self.example = example
        self.type = type
        self.description = description


class FolderProperties:
    context_type: ContentType
    context_id: FolderID
    files_count: FolderID
    position: FolderID
    updated_at: ContentType
    folders_url: ContentType
    files_url: ContentType
    full_name: ContentType
    lock_at: ContentType
    id: FolderID
    folders_count: FolderID
    name: ContentType
    parent_folder_id: FolderID
    created_at: ContentType
    unlock_at: ThumbnailURL
    hidden: Hidden
    hidden_for_user: Hidden
    locked: Hidden
    locked_for_user: Hidden
    for_submissions: ForSubmissions

    def __init__(self, context_type: ContentType, context_id: FolderID, files_count: FolderID, position: FolderID, updated_at: ContentType, folders_url: ContentType, files_url: ContentType, full_name: ContentType, lock_at: ContentType, id: FolderID, folders_count: FolderID, name: ContentType, parent_folder_id: FolderID, created_at: ContentType, unlock_at: ThumbnailURL, hidden: Hidden, hidden_for_user: Hidden, locked: Hidden, locked_for_user: Hidden, for_submissions: ForSubmissions) -> None:
        self.context_type = context_type
        self.context_id = context_id
        self.files_count = files_count
        self.position = position
        self.updated_at = updated_at
        self.folders_url = folders_url
        self.files_url = files_url
        self.full_name = full_name
        self.lock_at = lock_at
        self.id = id
        self.folders_count = folders_count
        self.name = name
        self.parent_folder_id = parent_folder_id
        self.created_at = created_at
        self.unlock_at = unlock_at
        self.hidden = hidden
        self.hidden_for_user = hidden_for_user
        self.locked = locked
        self.locked_for_user = locked_for_user
        self.for_submissions = for_submissions


class Folder:
    id: RefEnum
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: FolderProperties

    def __init__(self, id: RefEnum, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: FolderProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class LicenseProperties:
    id: MediaEntryID
    name: MediaEntryID
    url: MediaEntryID

    def __init__(self, id: MediaEntryID, name: MediaEntryID, url: MediaEntryID) -> None:
        self.id = id
        self.name = name
        self.url = url


class License:
    id: RefEnum
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: LicenseProperties

    def __init__(self, id: RefEnum, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: LicenseProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class FileIDS:
    description: str
    type: ItemsType
    items: ThumbnailURL
    example: List[int]

    def __init__(self, description: str, type: ItemsType, items: ThumbnailURL, example: List[int]) -> None:
        self.description = description
        self.type = type
        self.items = items
        self.example = example


class UsageRightsProperties:
    legal_copyright: MediaEntryID
    use_justification: MediaEntryID
    license: MediaEntryID
    license_name: MediaEntryID
    message: MediaEntryID
    file_ids: FileIDS

    def __init__(self, legal_copyright: MediaEntryID, use_justification: MediaEntryID, license: MediaEntryID, license_name: MediaEntryID, message: MediaEntryID, file_ids: FileIDS) -> None:
        self.legal_copyright = legal_copyright
        self.use_justification = use_justification
        self.license = license
        self.license_name = license_name
        self.message = message
        self.file_ids = file_ids


class UsageRights:
    id: TypeEnum
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: UsageRightsProperties

    def __init__(self, id: TypeEnum, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: UsageRightsProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    file: File
    folder: Folder
    usage_rights: UsageRights
    license: License

    def __init__(self, file: File, folder: Folder, usage_rights: UsageRights, license: License) -> None:
        self.file = file
        self.folder = folder
        self.usage_rights = usage_rights
        self.license = license


class Welcome3:
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
