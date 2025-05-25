from enum import Enum
from typing import Optional, List, Any


class Items:
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


class TypeEnum(Enum):
    ARRAY = "array"
    BLUEPRINT_RESTRICTION = "BlueprintRestriction"
    BOOLEAN = "boolean"
    DATETIME = "datetime"
    DATE_TIME = "DateTime"
    INTEGER = "integer"
    MULTIPLE_BLUEPRINT_RESTRICTIONS = "multiple BlueprintRestrictions"
    STRING = "string"


class EndAt:
    type: TypeEnum

    def __init__(self, type: TypeEnum) -> None:
        self.type = type


class ParamType(Enum):
    FORM = "form"
    PATH = "path"
    QUERY = "query"


class Parameter:
    param_type: ParamType
    name: str
    description: str
    type: TypeEnum
    format: Optional[Format]
    required: bool
    deprecated: bool
    enum: Optional[List[str]]
    items: Optional[EndAt]

    def __init__(self, param_type: ParamType, name: str, description: str, type: TypeEnum, format: Optional[Format], required: bool, deprecated: bool, enum: Optional[List[str]], items: Optional[EndAt]) -> None:
        self.param_type = param_type
        self.name = name
        self.description = description
        self.type = type
        self.format = format
        self.required = required
        self.deprecated = deprecated
        self.enum = enum
        self.items = items


class ResponseField:
    name: str
    description: str
    deprecated: bool

    def __init__(self, name: str, description: str, deprecated: bool) -> None:
        self.name = name
        self.description = description
        self.deprecated = deprecated


class Operation:
    method: Method
    summary: str
    notes: str
    nickname: str
    parameters: List[Parameter]
    response_fields: List[ResponseField]
    deprecated: bool
    deprecation_description: str
    type: str
    items: Optional[Items]

    def __init__(self, method: Method, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[ResponseField], deprecated: bool, deprecation_description: str, type: str, items: Optional[Items]) -> None:
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


class AllowableValues:
    values: List[str]

    def __init__(self, values: List[str]) -> None:
        self.values = values


class ICS:
    description: str
    example: str
    type: TypeEnum
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: str, type: TypeEnum, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.allowable_values = allowable_values


class CalendarLinkProperties:
    ics: ICS

    def __init__(self, ics: ICS) -> None:
        self.ics = ics


class CalendarLink:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: CalendarLinkProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: CalendarLinkProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class AccessRestrictedByDate:
    description: str
    example: bool
    type: TypeEnum

    def __init__(self, description: str, example: bool, type: TypeEnum) -> None:
        self.description = description
        self.example = example
        self.type = type


class AccountID:
    description: str
    example: int
    type: TypeEnum

    def __init__(self, description: str, example: int, type: TypeEnum) -> None:
        self.description = description
        self.example = example
        self.type = type


class AllowStudentAssignmentEdits:
    example: bool
    type: TypeEnum

    def __init__(self, example: bool, type: TypeEnum) -> None:
        self.example = example
        self.type = type


class BlueprintRestrictionsExample:
    content: bool
    points: bool
    due_dates: bool
    availability_dates: bool

    def __init__(self, content: bool, points: bool, due_dates: bool, availability_dates: bool) -> None:
        self.content = content
        self.points = points
        self.due_dates = due_dates
        self.availability_dates = availability_dates


class BlueprintRestrictions:
    description: str
    example: BlueprintRestrictionsExample
    type: str

    def __init__(self, description: str, example: BlueprintRestrictionsExample, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class Assignment:
    content: bool
    points: bool

    def __init__(self, content: bool, points: bool) -> None:
        self.content = content
        self.points = points


class WikiPage:
    content: bool

    def __init__(self, content: bool) -> None:
        self.content = content


class BlueprintRestrictionsByObjectTypeExample:
    assignment: Assignment
    wiki_page: WikiPage

    def __init__(self, assignment: Assignment, wiki_page: WikiPage) -> None:
        self.assignment = assignment
        self.wiki_page = wiki_page


class BlueprintRestrictionsByObjectType:
    description: str
    example: BlueprintRestrictionsByObjectTypeExample
    type: str

    def __init__(self, description: str, example: BlueprintRestrictionsByObjectTypeExample, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class Calendar:
    description: str
    ref: str

    def __init__(self, description: str, ref: str) -> None:
        self.description = description
        self.ref = ref


class CourseFormat:
    example: str
    type: TypeEnum

    def __init__(self, example: str, type: TypeEnum) -> None:
        self.example = example
        self.type = type


class Enrollments:
    description: str
    type: TypeEnum
    items: Items

    def __init__(self, description: str, type: TypeEnum, items: Items) -> None:
        self.description = description
        self.type = type
        self.items = items


class ID:
    description: str
    type: TypeEnum

    def __init__(self, description: str, type: TypeEnum) -> None:
        self.description = description
        self.type = type


class PermissionsExample:
    create_discussion_topic: bool
    create_announcement: bool

    def __init__(self, create_discussion_topic: bool, create_announcement: bool) -> None:
        self.create_discussion_topic = create_discussion_topic
        self.create_announcement = create_announcement


class Permissions:
    description: str
    example: PermissionsExample
    type: str
    key: EndAt
    value: EndAt

    def __init__(self, description: str, example: PermissionsExample, type: str, key: EndAt, value: EndAt) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.key = key
        self.value = value


class StorageQuotaMB:
    example: int
    type: str

    def __init__(self, example: int, type: str) -> None:
        self.example = example
        self.type = type


class CourseProperties:
    id: AccountID
    sis_course_id: ID
    uuid: ICS
    integration_id: ID
    sis_import_id: AccountID
    name: ICS
    course_code: ICS
    original_name: ICS
    workflow_state: ICS
    account_id: AccountID
    root_account_id: AccountID
    enrollment_term_id: AccountID
    grading_periods: Enrollments
    grading_standard_id: AccountID
    grade_passback_setting: ICS
    created_at: ICS
    start_at: ICS
    end_at: ICS
    locale: ICS
    enrollments: Enrollments
    total_students: AccountID
    calendar: Calendar
    default_view: ICS
    syllabus_body: ICS
    needs_grading_count: AccountID
    term: Calendar
    course_progress: Calendar
    apply_assignment_group_weights: AccessRestrictedByDate
    permissions: Permissions
    is_public: AllowStudentAssignmentEdits
    is_public_to_auth_users: AllowStudentAssignmentEdits
    public_syllabus: AllowStudentAssignmentEdits
    public_syllabus_to_auth: AllowStudentAssignmentEdits
    public_description: ICS
    storage_quota_mb: StorageQuotaMB
    storage_quota_used_mb: StorageQuotaMB
    hide_final_grades: AllowStudentAssignmentEdits
    license: CourseFormat
    allow_student_assignment_edits: AllowStudentAssignmentEdits
    allow_wiki_comments: AllowStudentAssignmentEdits
    allow_student_forum_attachments: AllowStudentAssignmentEdits
    open_enrollment: AllowStudentAssignmentEdits
    self_enrollment: AllowStudentAssignmentEdits
    restrict_enrollments_to_course_dates: AllowStudentAssignmentEdits
    course_format: CourseFormat
    access_restricted_by_date: AccessRestrictedByDate
    time_zone: ICS
    blueprint: AccessRestrictedByDate
    blueprint_restrictions: BlueprintRestrictions
    blueprint_restrictions_by_object_type: BlueprintRestrictionsByObjectType
    template: AccessRestrictedByDate

    def __init__(self, id: AccountID, sis_course_id: ID, uuid: ICS, integration_id: ID, sis_import_id: AccountID, name: ICS, course_code: ICS, original_name: ICS, workflow_state: ICS, account_id: AccountID, root_account_id: AccountID, enrollment_term_id: AccountID, grading_periods: Enrollments, grading_standard_id: AccountID, grade_passback_setting: ICS, created_at: ICS, start_at: ICS, end_at: ICS, locale: ICS, enrollments: Enrollments, total_students: AccountID, calendar: Calendar, default_view: ICS, syllabus_body: ICS, needs_grading_count: AccountID, term: Calendar, course_progress: Calendar, apply_assignment_group_weights: AccessRestrictedByDate, permissions: Permissions, is_public: AllowStudentAssignmentEdits, is_public_to_auth_users: AllowStudentAssignmentEdits, public_syllabus: AllowStudentAssignmentEdits, public_syllabus_to_auth: AllowStudentAssignmentEdits, public_description: ICS, storage_quota_mb: StorageQuotaMB, storage_quota_used_mb: StorageQuotaMB, hide_final_grades: AllowStudentAssignmentEdits, license: CourseFormat, allow_student_assignment_edits: AllowStudentAssignmentEdits, allow_wiki_comments: AllowStudentAssignmentEdits, allow_student_forum_attachments: AllowStudentAssignmentEdits, open_enrollment: AllowStudentAssignmentEdits, self_enrollment: AllowStudentAssignmentEdits, restrict_enrollments_to_course_dates: AllowStudentAssignmentEdits, course_format: CourseFormat, access_restricted_by_date: AccessRestrictedByDate, time_zone: ICS, blueprint: AccessRestrictedByDate, blueprint_restrictions: BlueprintRestrictions, blueprint_restrictions_by_object_type: BlueprintRestrictionsByObjectType, template: AccessRestrictedByDate) -> None:
        self.id = id
        self.sis_course_id = sis_course_id
        self.uuid = uuid
        self.integration_id = integration_id
        self.sis_import_id = sis_import_id
        self.name = name
        self.course_code = course_code
        self.original_name = original_name
        self.workflow_state = workflow_state
        self.account_id = account_id
        self.root_account_id = root_account_id
        self.enrollment_term_id = enrollment_term_id
        self.grading_periods = grading_periods
        self.grading_standard_id = grading_standard_id
        self.grade_passback_setting = grade_passback_setting
        self.created_at = created_at
        self.start_at = start_at
        self.end_at = end_at
        self.locale = locale
        self.enrollments = enrollments
        self.total_students = total_students
        self.calendar = calendar
        self.default_view = default_view
        self.syllabus_body = syllabus_body
        self.needs_grading_count = needs_grading_count
        self.term = term
        self.course_progress = course_progress
        self.apply_assignment_group_weights = apply_assignment_group_weights
        self.permissions = permissions
        self.is_public = is_public
        self.is_public_to_auth_users = is_public_to_auth_users
        self.public_syllabus = public_syllabus
        self.public_syllabus_to_auth = public_syllabus_to_auth
        self.public_description = public_description
        self.storage_quota_mb = storage_quota_mb
        self.storage_quota_used_mb = storage_quota_used_mb
        self.hide_final_grades = hide_final_grades
        self.license = license
        self.allow_student_assignment_edits = allow_student_assignment_edits
        self.allow_wiki_comments = allow_wiki_comments
        self.allow_student_forum_attachments = allow_student_forum_attachments
        self.open_enrollment = open_enrollment
        self.self_enrollment = self_enrollment
        self.restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates
        self.course_format = course_format
        self.access_restricted_by_date = access_restricted_by_date
        self.time_zone = time_zone
        self.blueprint = blueprint
        self.blueprint_restrictions = blueprint_restrictions
        self.blueprint_restrictions_by_object_type = blueprint_restrictions_by_object_type
        self.template = template


class Course:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: CourseProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: CourseProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class CourseProgressProperties:
    requirement_count: AccountID
    requirement_completed_count: AccountID
    next_requirement_url: ICS
    completed_at: ICS

    def __init__(self, requirement_count: AccountID, requirement_completed_count: AccountID, next_requirement_url: ICS, completed_at: ICS) -> None:
        self.requirement_count = requirement_count
        self.requirement_completed_count = requirement_completed_count
        self.next_requirement_url = next_requirement_url
        self.completed_at = completed_at


class CourseProgress:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: CourseProgressProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: CourseProgressProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class TermProperties:
    id: StorageQuotaMB
    name: CourseFormat
    start_at: CourseFormat
    end_at: EndAt

    def __init__(self, id: StorageQuotaMB, name: CourseFormat, start_at: CourseFormat, end_at: EndAt) -> None:
        self.id = id
        self.name = name
        self.start_at = start_at
        self.end_at = end_at


class Term:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: TermProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: TermProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    term: Term
    course_progress: CourseProgress
    course: Course
    calendar_link: CalendarLink

    def __init__(self, term: Term, course_progress: CourseProgress, course: Course, calendar_link: CalendarLink) -> None:
        self.term = term
        self.course_progress = course_progress
        self.course = course
        self.calendar_link = calendar_link


class Welcome10:
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
