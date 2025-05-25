from enum import Enum
from typing import Optional, List, Any


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
    FLOAT = "float"
    INT64 = "int64"


class ItemsType(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    DATE_TIME = "DateTime"
    INTEGER = "integer"
    NUMBER = "number"
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


class AllowableValues:
    values: List[str]

    def __init__(self, values: List[str]) -> None:
        self.values = values


class AbGUIDItems:
    type: ItemsType

    def __init__(self, type: ItemsType) -> None:
        self.type = type


class AbGUID:
    description: str
    example: List[str]
    type: ItemsType
    items: AbGUIDItems
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: List[str], type: ItemsType, items: AbGUIDItems, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.items = items
        self.allowable_values = allowable_values


class ExampleElement:
    section_id: int
    needs_grading_count: int

    def __init__(self, section_id: int, needs_grading_count: int) -> None:
        self.section_id = section_id
        self.needs_grading_count = needs_grading_count


class AllDates:
    description: str
    type: ItemsType
    items: OperationItems
    example: Optional[List[ExampleElement]]

    def __init__(self, description: str, type: ItemsType, items: OperationItems, example: Optional[List[ExampleElement]]) -> None:
        self.description = description
        self.type = type
        self.items = items
        self.example = example


class AllowedAttempts:
    description: str
    example: int
    type: ItemsType

    def __init__(self, description: str, example: int, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class ID:
    description: str
    type: ItemsType

    def __init__(self, description: str, type: ItemsType) -> None:
        self.description = description
        self.type = type


class AnonymizeStudents:
    description: str
    example: bool
    type: ItemsType

    def __init__(self, description: str, example: bool, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class AssignmentVisibility:
    description: str
    example: List[int]
    type: ItemsType
    items: AbGUIDItems

    def __init__(self, description: str, example: List[int], type: ItemsType, items: AbGUIDItems) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.items = items


class CreatedAtType(Enum):
    BOOLEAN = "boolean"
    DATETIME = "datetime"
    STRING = "string"


class CreatedAt:
    description: str
    example: str
    type: CreatedAtType
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: str, type: CreatedAtType, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.allowable_values = allowable_values


class DiscussionTopic:
    description: str
    ref: str

    def __init__(self, description: str, ref: str) -> None:
        self.description = description
        self.ref = ref


class IntegrationDataExample:
    the_5678: str

    def __init__(self, the_5678: str) -> None:
        self.the_5678 = the_5678


class IntegrationData:
    example: IntegrationDataExample
    type: str
    description: str

    def __init__(self, example: IntegrationDataExample, type: str, description: str) -> None:
        self.example = example
        self.type = type
        self.description = description


class RubricSettingsExample:
    points_possible: int

    def __init__(self, points_possible: int) -> None:
        self.points_possible = points_possible


class RubricSettings:
    description: str
    example: RubricSettingsExample
    type: str

    def __init__(self, description: str, example: RubricSettingsExample, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class AssignmentProperties:
    id: AllowedAttempts
    name: CreatedAt
    description: CreatedAt
    created_at: CreatedAt
    updated_at: CreatedAt
    due_at: CreatedAt
    lock_at: CreatedAt
    unlock_at: CreatedAt
    has_overrides: AnonymizeStudents
    all_dates: AllDates
    course_id: AllowedAttempts
    html_url: CreatedAt
    submissions_download_url: CreatedAt
    assignment_group_id: AllowedAttempts
    due_date_required: AnonymizeStudents
    allowed_extensions: AbGUID
    max_name_length: AllowedAttempts
    turnitin_enabled: AnonymizeStudents
    vericite_enabled: AnonymizeStudents
    turnitin_settings: DiscussionTopic
    grade_group_students_individually: AnonymizeStudents
    external_tool_tag_attributes: DiscussionTopic
    peer_reviews: AnonymizeStudents
    automatic_peer_reviews: AnonymizeStudents
    peer_review_count: AllowedAttempts
    peer_reviews_assign_at: CreatedAt
    intra_group_peer_reviews: CreatedAt
    group_category_id: AllowedAttempts
    needs_grading_count: AllowedAttempts
    needs_grading_count_by_section: AllDates
    position: AllowedAttempts
    post_to_sis: AnonymizeStudents
    integration_id: CreatedAt
    integration_data: IntegrationData
    points_possible: AllowedAttempts
    submission_types: AbGUID
    has_submitted_submissions: AnonymizeStudents
    grading_type: CreatedAt
    grading_standard_id: ID
    published: AnonymizeStudents
    unpublishable: AnonymizeStudents
    only_visible_to_overrides: AnonymizeStudents
    locked_for_user: AnonymizeStudents
    lock_info: DiscussionTopic
    lock_explanation: CreatedAt
    quiz_id: AllowedAttempts
    anonymous_submissions: AnonymizeStudents
    discussion_topic: DiscussionTopic
    freeze_on_copy: AnonymizeStudents
    frozen: AnonymizeStudents
    frozen_attributes: AbGUID
    submission: DiscussionTopic
    use_rubric_for_grading: AnonymizeStudents
    rubric_settings: RubricSettings
    rubric: AllDates
    assignment_visibility: AssignmentVisibility
    overrides: AllDates
    omit_from_final_grade: AnonymizeStudents
    hide_in_gradebook: AnonymizeStudents
    moderated_grading: AnonymizeStudents
    grader_count: AllowedAttempts
    final_grader_id: AllowedAttempts
    grader_comments_visible_to_graders: AnonymizeStudents
    graders_anonymous_to_graders: AnonymizeStudents
    grader_names_visible_to_final_grader: AnonymizeStudents
    anonymous_grading: AnonymizeStudents
    allowed_attempts: AllowedAttempts
    post_manually: AnonymizeStudents
    score_statistics: DiscussionTopic
    can_submit: AnonymizeStudents
    ab_guid: AbGUID
    annotatable_attachment_id: ID
    anonymize_students: AnonymizeStudents
    require_lockdown_browser: AnonymizeStudents
    important_dates: AnonymizeStudents
    muted: AnonymizeStudents
    anonymous_peer_reviews: AnonymizeStudents
    anonymous_instructor_annotations: AnonymizeStudents
    graded_submissions_exist: AnonymizeStudents
    is_quiz_assignment: AnonymizeStudents
    in_closed_grading_period: AnonymizeStudents
    can_duplicate: AnonymizeStudents
    original_course_id: AllowedAttempts
    original_assignment_id: AllowedAttempts
    original_lti_resource_link_id: AllowedAttempts
    original_assignment_name: CreatedAt
    original_quiz_id: AllowedAttempts
    workflow_state: CreatedAt

    def __init__(self, id: AllowedAttempts, name: CreatedAt, description: CreatedAt, created_at: CreatedAt, updated_at: CreatedAt, due_at: CreatedAt, lock_at: CreatedAt, unlock_at: CreatedAt, has_overrides: AnonymizeStudents, all_dates: AllDates, course_id: AllowedAttempts, html_url: CreatedAt, submissions_download_url: CreatedAt, assignment_group_id: AllowedAttempts, due_date_required: AnonymizeStudents, allowed_extensions: AbGUID, max_name_length: AllowedAttempts, turnitin_enabled: AnonymizeStudents, vericite_enabled: AnonymizeStudents, turnitin_settings: DiscussionTopic, grade_group_students_individually: AnonymizeStudents, external_tool_tag_attributes: DiscussionTopic, peer_reviews: AnonymizeStudents, automatic_peer_reviews: AnonymizeStudents, peer_review_count: AllowedAttempts, peer_reviews_assign_at: CreatedAt, intra_group_peer_reviews: CreatedAt, group_category_id: AllowedAttempts, needs_grading_count: AllowedAttempts, needs_grading_count_by_section: AllDates, position: AllowedAttempts, post_to_sis: AnonymizeStudents, integration_id: CreatedAt, integration_data: IntegrationData, points_possible: AllowedAttempts, submission_types: AbGUID, has_submitted_submissions: AnonymizeStudents, grading_type: CreatedAt, grading_standard_id: ID, published: AnonymizeStudents, unpublishable: AnonymizeStudents, only_visible_to_overrides: AnonymizeStudents, locked_for_user: AnonymizeStudents, lock_info: DiscussionTopic, lock_explanation: CreatedAt, quiz_id: AllowedAttempts, anonymous_submissions: AnonymizeStudents, discussion_topic: DiscussionTopic, freeze_on_copy: AnonymizeStudents, frozen: AnonymizeStudents, frozen_attributes: AbGUID, submission: DiscussionTopic, use_rubric_for_grading: AnonymizeStudents, rubric_settings: RubricSettings, rubric: AllDates, assignment_visibility: AssignmentVisibility, overrides: AllDates, omit_from_final_grade: AnonymizeStudents, hide_in_gradebook: AnonymizeStudents, moderated_grading: AnonymizeStudents, grader_count: AllowedAttempts, final_grader_id: AllowedAttempts, grader_comments_visible_to_graders: AnonymizeStudents, graders_anonymous_to_graders: AnonymizeStudents, grader_names_visible_to_final_grader: AnonymizeStudents, anonymous_grading: AnonymizeStudents, allowed_attempts: AllowedAttempts, post_manually: AnonymizeStudents, score_statistics: DiscussionTopic, can_submit: AnonymizeStudents, ab_guid: AbGUID, annotatable_attachment_id: ID, anonymize_students: AnonymizeStudents, require_lockdown_browser: AnonymizeStudents, important_dates: AnonymizeStudents, muted: AnonymizeStudents, anonymous_peer_reviews: AnonymizeStudents, anonymous_instructor_annotations: AnonymizeStudents, graded_submissions_exist: AnonymizeStudents, is_quiz_assignment: AnonymizeStudents, in_closed_grading_period: AnonymizeStudents, can_duplicate: AnonymizeStudents, original_course_id: AllowedAttempts, original_assignment_id: AllowedAttempts, original_lti_resource_link_id: AllowedAttempts, original_assignment_name: CreatedAt, original_quiz_id: AllowedAttempts, workflow_state: CreatedAt) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.due_at = due_at
        self.lock_at = lock_at
        self.unlock_at = unlock_at
        self.has_overrides = has_overrides
        self.all_dates = all_dates
        self.course_id = course_id
        self.html_url = html_url
        self.submissions_download_url = submissions_download_url
        self.assignment_group_id = assignment_group_id
        self.due_date_required = due_date_required
        self.allowed_extensions = allowed_extensions
        self.max_name_length = max_name_length
        self.turnitin_enabled = turnitin_enabled
        self.vericite_enabled = vericite_enabled
        self.turnitin_settings = turnitin_settings
        self.grade_group_students_individually = grade_group_students_individually
        self.external_tool_tag_attributes = external_tool_tag_attributes
        self.peer_reviews = peer_reviews
        self.automatic_peer_reviews = automatic_peer_reviews
        self.peer_review_count = peer_review_count
        self.peer_reviews_assign_at = peer_reviews_assign_at
        self.intra_group_peer_reviews = intra_group_peer_reviews
        self.group_category_id = group_category_id
        self.needs_grading_count = needs_grading_count
        self.needs_grading_count_by_section = needs_grading_count_by_section
        self.position = position
        self.post_to_sis = post_to_sis
        self.integration_id = integration_id
        self.integration_data = integration_data
        self.points_possible = points_possible
        self.submission_types = submission_types
        self.has_submitted_submissions = has_submitted_submissions
        self.grading_type = grading_type
        self.grading_standard_id = grading_standard_id
        self.published = published
        self.unpublishable = unpublishable
        self.only_visible_to_overrides = only_visible_to_overrides
        self.locked_for_user = locked_for_user
        self.lock_info = lock_info
        self.lock_explanation = lock_explanation
        self.quiz_id = quiz_id
        self.anonymous_submissions = anonymous_submissions
        self.discussion_topic = discussion_topic
        self.freeze_on_copy = freeze_on_copy
        self.frozen = frozen
        self.frozen_attributes = frozen_attributes
        self.submission = submission
        self.use_rubric_for_grading = use_rubric_for_grading
        self.rubric_settings = rubric_settings
        self.rubric = rubric
        self.assignment_visibility = assignment_visibility
        self.overrides = overrides
        self.omit_from_final_grade = omit_from_final_grade
        self.hide_in_gradebook = hide_in_gradebook
        self.moderated_grading = moderated_grading
        self.grader_count = grader_count
        self.final_grader_id = final_grader_id
        self.grader_comments_visible_to_graders = grader_comments_visible_to_graders
        self.graders_anonymous_to_graders = graders_anonymous_to_graders
        self.grader_names_visible_to_final_grader = grader_names_visible_to_final_grader
        self.anonymous_grading = anonymous_grading
        self.allowed_attempts = allowed_attempts
        self.post_manually = post_manually
        self.score_statistics = score_statistics
        self.can_submit = can_submit
        self.ab_guid = ab_guid
        self.annotatable_attachment_id = annotatable_attachment_id
        self.anonymize_students = anonymize_students
        self.require_lockdown_browser = require_lockdown_browser
        self.important_dates = important_dates
        self.muted = muted
        self.anonymous_peer_reviews = anonymous_peer_reviews
        self.anonymous_instructor_annotations = anonymous_instructor_annotations
        self.graded_submissions_exist = graded_submissions_exist
        self.is_quiz_assignment = is_quiz_assignment
        self.in_closed_grading_period = in_closed_grading_period
        self.can_duplicate = can_duplicate
        self.original_course_id = original_course_id
        self.original_assignment_id = original_assignment_id
        self.original_lti_resource_link_id = original_lti_resource_link_id
        self.original_assignment_name = original_assignment_name
        self.original_quiz_id = original_quiz_id
        self.workflow_state = workflow_state


class Assignment:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: AssignmentProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: AssignmentProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Title:
    example: str
    type: ItemsType

    def __init__(self, example: str, type: ItemsType) -> None:
        self.example = example
        self.type = type


class AssignmentDateProperties:
    id: AllowedAttempts
    base: AnonymizeStudents
    title: Title
    due_at: CreatedAt
    unlock_at: CreatedAt
    lock_at: CreatedAt

    def __init__(self, id: AllowedAttempts, base: AnonymizeStudents, title: Title, due_at: CreatedAt, unlock_at: CreatedAt, lock_at: CreatedAt) -> None:
        self.id = id
        self.base = base
        self.title = title
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.lock_at = lock_at


class AssignmentDate:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: AssignmentDateProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: AssignmentDateProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class AssignmentOverrideProperties:
    id: AllowedAttempts
    assignment_id: AllowedAttempts
    quiz_id: AllowedAttempts
    context_module_id: AllowedAttempts
    discussion_topic_id: AllowedAttempts
    wiki_page_id: AllowedAttempts
    attachment_id: AllowedAttempts
    student_ids: AssignmentVisibility
    group_id: AllowedAttempts
    course_section_id: AllowedAttempts
    title: CreatedAt
    due_at: CreatedAt
    all_day: AnonymizeStudents
    all_day_date: CreatedAt
    unlock_at: CreatedAt
    lock_at: CreatedAt

    def __init__(self, id: AllowedAttempts, assignment_id: AllowedAttempts, quiz_id: AllowedAttempts, context_module_id: AllowedAttempts, discussion_topic_id: AllowedAttempts, wiki_page_id: AllowedAttempts, attachment_id: AllowedAttempts, student_ids: AssignmentVisibility, group_id: AllowedAttempts, course_section_id: AllowedAttempts, title: CreatedAt, due_at: CreatedAt, all_day: AnonymizeStudents, all_day_date: CreatedAt, unlock_at: CreatedAt, lock_at: CreatedAt) -> None:
        self.id = id
        self.assignment_id = assignment_id
        self.quiz_id = quiz_id
        self.context_module_id = context_module_id
        self.discussion_topic_id = discussion_topic_id
        self.wiki_page_id = wiki_page_id
        self.attachment_id = attachment_id
        self.student_ids = student_ids
        self.group_id = group_id
        self.course_section_id = course_section_id
        self.title = title
        self.due_at = due_at
        self.all_day = all_day
        self.all_day_date = all_day_date
        self.unlock_at = unlock_at
        self.lock_at = lock_at


class AssignmentOverride:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: AssignmentOverrideProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: AssignmentOverrideProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class BasicUserProperties:
    id: CreatedAt
    name: CreatedAt

    def __init__(self, id: CreatedAt, name: CreatedAt) -> None:
        self.id = id
        self.name = name


class BasicUser:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: BasicUserProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: BasicUserProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class ExternalToolTagAttributesProperties:
    url: CreatedAt
    new_tab: AnonymizeStudents
    resource_link_id: CreatedAt

    def __init__(self, url: CreatedAt, new_tab: AnonymizeStudents, resource_link_id: CreatedAt) -> None:
        self.url = url
        self.new_tab = new_tab
        self.resource_link_id = resource_link_id


class ExternalToolTagAttributes:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ExternalToolTagAttributesProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ExternalToolTagAttributesProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class ManuallyLocked:
    example: bool
    type: ItemsType

    def __init__(self, example: bool, type: ItemsType) -> None:
        self.example = example
        self.type = type


class LockInfoProperties:
    asset_string: CreatedAt
    unlock_at: CreatedAt
    lock_at: CreatedAt
    context_module: CreatedAt
    manually_locked: ManuallyLocked

    def __init__(self, asset_string: CreatedAt, unlock_at: CreatedAt, lock_at: CreatedAt, context_module: CreatedAt, manually_locked: ManuallyLocked) -> None:
        self.asset_string = asset_string
        self.unlock_at = unlock_at
        self.lock_at = lock_at
        self.context_module = context_module
        self.manually_locked = manually_locked


class LockInfo:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: LockInfoProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: LockInfoProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class NeedsGradingCountProperties:
    section_id: CreatedAt
    needs_grading_count: AllowedAttempts

    def __init__(self, section_id: CreatedAt, needs_grading_count: AllowedAttempts) -> None:
        self.section_id = section_id
        self.needs_grading_count = needs_grading_count


class NeedsGradingCount:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: NeedsGradingCountProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: NeedsGradingCountProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Points:
    example: int
    type: ItemsType

    def __init__(self, example: int, type: ItemsType) -> None:
        self.example = example
        self.type = type


class Ratings:
    type: ItemsType
    items: OperationItems

    def __init__(self, type: ItemsType, items: OperationItems) -> None:
        self.type = type
        self.items = items


class RubricCriteriaProperties:
    points: Points
    id: CreatedAt
    learning_outcome_id: CreatedAt
    vendor_guid: CreatedAt
    description: Title
    long_description: Title
    criterion_use_range: ManuallyLocked
    ratings: Ratings
    ignore_for_scoring: ManuallyLocked

    def __init__(self, points: Points, id: CreatedAt, learning_outcome_id: CreatedAt, vendor_guid: CreatedAt, description: Title, long_description: Title, criterion_use_range: ManuallyLocked, ratings: Ratings, ignore_for_scoring: ManuallyLocked) -> None:
        self.points = points
        self.id = id
        self.learning_outcome_id = learning_outcome_id
        self.vendor_guid = vendor_guid
        self.description = description
        self.long_description = long_description
        self.criterion_use_range = criterion_use_range
        self.ratings = ratings
        self.ignore_for_scoring = ignore_for_scoring


class RubricCriteria:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricCriteriaProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricCriteriaProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class RubricRatingProperties:
    points: Points
    id: Title
    description: Title
    long_description: Title

    def __init__(self, points: Points, id: Title, description: Title, long_description: Title) -> None:
        self.points = points
        self.id = id
        self.description = description
        self.long_description = long_description


class RubricRating:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricRatingProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricRatingProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class ScoreStatisticProperties:
    min: AllowedAttempts
    max: AllowedAttempts
    mean: AllowedAttempts
    upper_q: AllowedAttempts
    median: AllowedAttempts
    lower_q: AllowedAttempts

    def __init__(self, min: AllowedAttempts, max: AllowedAttempts, mean: AllowedAttempts, upper_q: AllowedAttempts, median: AllowedAttempts, lower_q: AllowedAttempts) -> None:
        self.min = min
        self.max = max
        self.mean = mean
        self.upper_q = upper_q
        self.median = median
        self.lower_q = lower_q


class ScoreStatistic:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: ScoreStatisticProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: ScoreStatisticProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class TurnitinSettingsProperties:
    originality_report_visibility: Title
    s_paper_check: ManuallyLocked
    internet_check: ManuallyLocked
    journal_check: ManuallyLocked
    exclude_biblio: ManuallyLocked
    exclude_quoted: ManuallyLocked
    exclude_small_matches_type: Title
    exclude_small_matches_value: Points

    def __init__(self, originality_report_visibility: Title, s_paper_check: ManuallyLocked, internet_check: ManuallyLocked, journal_check: ManuallyLocked, exclude_biblio: ManuallyLocked, exclude_quoted: ManuallyLocked, exclude_small_matches_type: Title, exclude_small_matches_value: Points) -> None:
        self.originality_report_visibility = originality_report_visibility
        self.s_paper_check = s_paper_check
        self.internet_check = internet_check
        self.journal_check = journal_check
        self.exclude_biblio = exclude_biblio
        self.exclude_quoted = exclude_quoted
        self.exclude_small_matches_type = exclude_small_matches_type
        self.exclude_small_matches_value = exclude_small_matches_value


class TurnitinSettings:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: TurnitinSettingsProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: TurnitinSettingsProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    external_tool_tag_attributes: ExternalToolTagAttributes
    lock_info: LockInfo
    rubric_rating: RubricRating
    rubric_criteria: RubricCriteria
    assignment_date: AssignmentDate
    turnitin_settings: TurnitinSettings
    needs_grading_count: NeedsGradingCount
    score_statistic: ScoreStatistic
    assignment: Assignment
    basic_user: BasicUser
    assignment_override: AssignmentOverride

    def __init__(self, external_tool_tag_attributes: ExternalToolTagAttributes, lock_info: LockInfo, rubric_rating: RubricRating, rubric_criteria: RubricCriteria, assignment_date: AssignmentDate, turnitin_settings: TurnitinSettings, needs_grading_count: NeedsGradingCount, score_statistic: ScoreStatistic, assignment: Assignment, basic_user: BasicUser, assignment_override: AssignmentOverride) -> None:
        self.external_tool_tag_attributes = external_tool_tag_attributes
        self.lock_info = lock_info
        self.rubric_rating = rubric_rating
        self.rubric_criteria = rubric_criteria
        self.assignment_date = assignment_date
        self.turnitin_settings = turnitin_settings
        self.needs_grading_count = needs_grading_count
        self.score_statistic = score_statistic
        self.assignment = assignment
        self.basic_user = basic_user
        self.assignment_override = assignment_override


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
