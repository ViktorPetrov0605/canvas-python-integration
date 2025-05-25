from enum import Enum
from typing import Optional, List, Any
from datetime import datetime


class OperationItems:
    ref: str

    def __init__(self, ref: str) -> None:
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


class ParameterItems:
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
    enum: Optional[List[str]]
    items: Optional[ParameterItems]

    def __init__(self, param_type: ParamType, name: str, description: str, type: ItemsType, format: Optional[Format], required: bool, deprecated: bool, enum: Optional[List[str]], items: Optional[ParameterItems]) -> None:
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
    method: Method
    summary: str
    notes: str
    nickname: str
    parameters: List[Parameter]
    response_fields: List[Any]
    deprecated: bool
    deprecation_description: str
    type: str
    items: Optional[OperationItems]

    def __init__(self, method: Method, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[Any], deprecated: bool, deprecation_description: str, type: str, items: Optional[OperationItems]) -> None:
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


class Completed:
    description: str
    example: bool
    type: ItemsType

    def __init__(self, description: str, example: bool, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class MinPercentage:
    description: str
    example: int
    type: ItemsType

    def __init__(self, description: str, example: int, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class AllowableValues:
    values: List[str]

    def __init__(self, values: List[str]) -> None:
        self.values = values


class TypeType(Enum):
    DATETIME = "datetime"
    STRING = "string"


class TypeClass:
    description: str
    example: str
    type: TypeType
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: str, type: TypeType, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.allowable_values = allowable_values


class CompletionRequirementProperties:
    type: TypeClass
    min_score: MinPercentage
    min_percentage: MinPercentage
    completed: Completed

    def __init__(self, type: TypeClass, min_score: MinPercentage, min_percentage: MinPercentage, completed: Completed) -> None:
        self.type = type
        self.min_score = min_score
        self.min_percentage = min_percentage
        self.completed = completed


class CompletionRequirement:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: CompletionRequirementProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: CompletionRequirementProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class DueAt:
    example: str
    type: TypeType

    def __init__(self, example: str, type: TypeType) -> None:
        self.example = example
        self.type = type


class ContextModule:
    pass

    def __init__(self, ) -> None:
        pass


class LockInfoExample:
    asset_string: str
    unlock_at: datetime
    lock_at: datetime
    context_module: ContextModule

    def __init__(self, asset_string: str, unlock_at: datetime, lock_at: datetime, context_module: ContextModule) -> None:
        self.asset_string = asset_string
        self.unlock_at = unlock_at
        self.lock_at = lock_at
        self.context_module = context_module


class LockInfo:
    example: LockInfoExample
    ref: str

    def __init__(self, example: LockInfoExample, ref: str) -> None:
        self.example = example
        self.ref = ref


class LockedForUser:
    example: bool
    type: ItemsType

    def __init__(self, example: bool, type: ItemsType) -> None:
        self.example = example
        self.type = type


class PointsPossible:
    example: int
    type: ItemsType

    def __init__(self, example: int, type: ItemsType) -> None:
        self.example = example
        self.type = type


class ContentDetailsProperties:
    points_possible: PointsPossible
    due_at: DueAt
    unlock_at: DueAt
    lock_at: DueAt
    locked_for_user: LockedForUser
    lock_explanation: DueAt
    lock_info: LockInfo

    def __init__(self, points_possible: PointsPossible, due_at: DueAt, unlock_at: DueAt, lock_at: DueAt, locked_for_user: LockedForUser, lock_explanation: DueAt, lock_info: LockInfo) -> None:
        self.points_possible = points_possible
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.lock_at = lock_at
        self.locked_for_user = locked_for_user
        self.lock_explanation = lock_explanation
        self.lock_info = lock_info


class ContentDetails:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ContentDetailsProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ContentDetailsProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class CompletedAt:
    description: str
    type: str

    def __init__(self, description: str, type: str) -> None:
        self.description = description
        self.type = type


class CurrentClass:
    id: int
    module_id: int
    title: str
    type: str

    def __init__(self, id: int, module_id: int, title: str, type: str) -> None:
        self.id = id
        self.module_id = module_id
        self.title = title
        self.type = type


class MasteryPathClass:
    locked: bool
    assignment_sets: List[Any]
    selected_set_id: None
    awaiting_choice: bool
    still_processing: bool
    modules_url: str
    choose_url: str
    modules_tab_disabled: bool

    def __init__(self, locked: bool, assignment_sets: List[Any], selected_set_id: None, awaiting_choice: bool, still_processing: bool, modules_url: str, choose_url: str, modules_tab_disabled: bool) -> None:
        self.locked = locked
        self.assignment_sets = assignment_sets
        self.selected_set_id = selected_set_id
        self.awaiting_choice = awaiting_choice
        self.still_processing = still_processing
        self.modules_url = modules_url
        self.choose_url = choose_url
        self.modules_tab_disabled = modules_tab_disabled


class ExampleElement:
    prev: None
    current: Optional[CurrentClass]
    next: Optional[CurrentClass]
    mastery_path: Optional[MasteryPathClass]
    id: Optional[int]
    name: Optional[str]

    def __init__(self, prev: None, current: Optional[CurrentClass], next: Optional[CurrentClass], mastery_path: Optional[MasteryPathClass], id: Optional[int], name: Optional[str]) -> None:
        self.prev = prev
        self.current = current
        self.next = next
        self.mastery_path = mastery_path
        self.id = id
        self.name = name


class ModulesClass:
    description: str
    type: ItemsType
    items: OperationItems
    example: Optional[List[ExampleElement]]

    def __init__(self, description: str, type: ItemsType, items: OperationItems, example: Optional[List[ExampleElement]]) -> None:
        self.description = description
        self.type = type
        self.items = items
        self.example = example


class PrerequisiteModuleIDSItems:
    type: ItemsType

    def __init__(self, type: ItemsType) -> None:
        self.type = type


class PrerequisiteModuleIDS:
    description: str
    example: List[int]
    type: ItemsType
    items: PrerequisiteModuleIDSItems

    def __init__(self, description: str, example: List[int], type: ItemsType, items: PrerequisiteModuleIDSItems) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.items = items


class ModuleProperties:
    id: MinPercentage
    workflow_state: TypeClass
    position: MinPercentage
    name: TypeClass
    unlock_at: TypeClass
    require_sequential_progress: Completed
    requirement_type: TypeClass
    prerequisite_module_ids: PrerequisiteModuleIDS
    items_count: MinPercentage
    items_url: TypeClass
    items: ModulesClass
    state: TypeClass
    completed_at: CompletedAt
    publish_final_grade: CompletedAt
    published: Completed

    def __init__(self, id: MinPercentage, workflow_state: TypeClass, position: MinPercentage, name: TypeClass, unlock_at: TypeClass, require_sequential_progress: Completed, requirement_type: TypeClass, prerequisite_module_ids: PrerequisiteModuleIDS, items_count: MinPercentage, items_url: TypeClass, items: ModulesClass, state: TypeClass, completed_at: CompletedAt, publish_final_grade: CompletedAt, published: Completed) -> None:
        self.id = id
        self.workflow_state = workflow_state
        self.position = position
        self.name = name
        self.unlock_at = unlock_at
        self.require_sequential_progress = require_sequential_progress
        self.requirement_type = requirement_type
        self.prerequisite_module_ids = prerequisite_module_ids
        self.items_count = items_count
        self.items_url = items_url
        self.items = items
        self.state = state
        self.completed_at = completed_at
        self.publish_final_grade = publish_final_grade
        self.published = published


class Module:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ModuleProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ModuleProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class CourseSection:
    description: str
    ref: str

    def __init__(self, description: str, ref: str) -> None:
        self.description = description
        self.ref = ref


class ModuleAssignmentOverrideProperties:
    id: MinPercentage
    context_module_id: MinPercentage
    title: TypeClass
    students: CourseSection
    course_section: CourseSection

    def __init__(self, id: MinPercentage, context_module_id: MinPercentage, title: TypeClass, students: CourseSection, course_section: CourseSection) -> None:
        self.id = id
        self.context_module_id = context_module_id
        self.title = title
        self.students = students
        self.course_section = course_section


class ModuleAssignmentOverride:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ModuleAssignmentOverrideProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ModuleAssignmentOverrideProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class CompletionRequirementExample:
    type: str
    min_score: int
    completed: bool

    def __init__(self, type: str, min_score: int, completed: bool) -> None:
        self.type = type
        self.min_score = min_score
        self.completed = completed


class CompletionRequirementClass:
    description: str
    example: CompletionRequirementExample
    ref: str

    def __init__(self, description: str, example: CompletionRequirementExample, ref: str) -> None:
        self.description = description
        self.example = example
        self.ref = ref


class ContentDetailsExample:
    points_possible: int
    due_at: datetime
    unlock_at: datetime
    lock_at: datetime

    def __init__(self, points_possible: int, due_at: datetime, unlock_at: datetime, lock_at: datetime) -> None:
        self.points_possible = points_possible
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.lock_at = lock_at


class ContentDetailsClass:
    description: str
    example: ContentDetailsExample
    ref: str

    def __init__(self, description: str, example: ContentDetailsExample, ref: str) -> None:
        self.description = description
        self.example = example
        self.ref = ref


class ModuleItemProperties:
    id: MinPercentage
    module_id: MinPercentage
    position: MinPercentage
    title: TypeClass
    indent: MinPercentage
    type: TypeClass
    content_id: MinPercentage
    html_url: TypeClass
    url: TypeClass
    page_url: TypeClass
    external_url: TypeClass
    new_tab: Completed
    completion_requirement: CompletionRequirementClass
    content_details: ContentDetailsClass
    published: Completed

    def __init__(self, id: MinPercentage, module_id: MinPercentage, position: MinPercentage, title: TypeClass, indent: MinPercentage, type: TypeClass, content_id: MinPercentage, html_url: TypeClass, url: TypeClass, page_url: TypeClass, external_url: TypeClass, new_tab: Completed, completion_requirement: CompletionRequirementClass, content_details: ContentDetailsClass, published: Completed) -> None:
        self.id = id
        self.module_id = module_id
        self.position = position
        self.title = title
        self.indent = indent
        self.type = type
        self.content_id = content_id
        self.html_url = html_url
        self.url = url
        self.page_url = page_url
        self.external_url = external_url
        self.new_tab = new_tab
        self.completion_requirement = completion_requirement
        self.content_details = content_details
        self.published = published


class ModuleItem:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ModuleItemProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ModuleItemProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class ModuleItemSequenceProperties:
    items: ModulesClass
    modules: ModulesClass

    def __init__(self, items: ModulesClass, modules: ModulesClass) -> None:
        self.items = items
        self.modules = modules


class ModuleItemSequence:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ModuleItemSequenceProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ModuleItemSequenceProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Current:
    description: str
    ref: str
    example: CurrentClass

    def __init__(self, description: str, ref: str, example: CurrentClass) -> None:
        self.description = description
        self.ref = ref
        self.example = example


class MasteryPath:
    type: str
    description: str
    example: MasteryPathClass

    def __init__(self, type: str, description: str, example: MasteryPathClass) -> None:
        self.type = type
        self.description = description
        self.example = example


class ModuleItemSequenceNodeProperties:
    prev: CourseSection
    current: Current
    next: Current
    mastery_path: MasteryPath

    def __init__(self, prev: CourseSection, current: Current, next: Current, mastery_path: MasteryPath) -> None:
        self.prev = prev
        self.current = current
        self.next = next
        self.mastery_path = mastery_path


class ModuleItemSequenceNode:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ModuleItemSequenceNodeProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ModuleItemSequenceNodeProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class OverrideTargetProperties:
    id: MinPercentage
    name: TypeClass

    def __init__(self, id: MinPercentage, name: TypeClass) -> None:
        self.id = id
        self.name = name


class OverrideTarget:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: OverrideTargetProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: OverrideTargetProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    module: Module
    completion_requirement: CompletionRequirement
    content_details: ContentDetails
    module_item: ModuleItem
    module_item_sequence_node: ModuleItemSequenceNode
    module_item_sequence: ModuleItemSequence
    module_assignment_override: ModuleAssignmentOverride
    override_target: OverrideTarget

    def __init__(self, module: Module, completion_requirement: CompletionRequirement, content_details: ContentDetails, module_item: ModuleItem, module_item_sequence_node: ModuleItemSequenceNode, module_item_sequence: ModuleItemSequence, module_assignment_override: ModuleAssignmentOverride, override_target: OverrideTarget) -> None:
        self.module = module
        self.completion_requirement = completion_requirement
        self.content_details = content_details
        self.module_item = module_item
        self.module_item_sequence_node = module_item_sequence_node
        self.module_item_sequence = module_item_sequence
        self.module_assignment_override = module_assignment_override
        self.override_target = override_target


class Welcome2:
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
