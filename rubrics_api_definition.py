from enum import Enum
from typing import Optional, List, Any


class Method(Enum):
    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class Format(Enum):
    INT64 = "int64"


class Description:
    type: str

    def __init__(self, type: str) -> None:
        self.type = type


class ParamType(Enum):
    FORM = "form"
    PATH = "path"
    QUERY = "query"


class TypeEnum(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    HASH = "Hash"
    INTEGER = "integer"
    STRING = "string"


class Parameter:
    param_type: ParamType
    name: str
    description: str
    type: TypeEnum
    format: Optional[Format]
    required: bool
    deprecated: bool
    enum: Optional[List[str]]
    items: Optional[Description]

    def __init__(self, param_type: ParamType, name: str, description: str, type: TypeEnum, format: Optional[Format], required: bool, deprecated: bool, enum: Optional[List[str]], items: Optional[Description]) -> None:
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

    def __init__(self, method: Method, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[Any], deprecated: bool, deprecation_description: str, type: str) -> None:
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


class Items:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref


class Assessments:
    description: str
    type: TypeEnum
    items: Items

    def __init__(self, description: str, type: TypeEnum, items: Items) -> None:
        self.description = description
        self.type = type
        self.items = items


class ContextID:
    description: str
    example: int
    type: TypeEnum

    def __init__(self, description: str, example: int, type: TypeEnum) -> None:
        self.description = description
        self.example = example
        self.type = type


class ContextType:
    example: str
    type: TypeEnum

    def __init__(self, example: str, type: TypeEnum) -> None:
        self.example = example
        self.type = type


class FreeFormCriterionComments:
    description: str
    example: str
    type: TypeEnum

    def __init__(self, description: str, example: str, type: TypeEnum) -> None:
        self.description = description
        self.example = example
        self.type = type


class RubricProperties:
    id: ContextID
    title: FreeFormCriterionComments
    context_id: ContextID
    context_type: ContextType
    points_possible: ContextType
    reusable: ContextType
    read_only: ContextType
    free_form_criterion_comments: FreeFormCriterionComments
    hide_score_total: ContextType
    data: Assessments
    assessments: Assessments
    associations: Assessments

    def __init__(self, id: ContextID, title: FreeFormCriterionComments, context_id: ContextID, context_type: ContextType, points_possible: ContextType, reusable: ContextType, read_only: ContextType, free_form_criterion_comments: FreeFormCriterionComments, hide_score_total: ContextType, data: Assessments, assessments: Assessments, associations: Assessments) -> None:
        self.id = id
        self.title = title
        self.context_id = context_id
        self.context_type = context_type
        self.points_possible = points_possible
        self.reusable = reusable
        self.read_only = read_only
        self.free_form_criterion_comments = free_form_criterion_comments
        self.hide_score_total = hide_score_total
        self.data = data
        self.assessments = assessments
        self.associations = associations


class Rubric:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Comments:
    description: str
    type: TypeEnum
    items: Description

    def __init__(self, description: str, type: TypeEnum, items: Description) -> None:
        self.description = description
        self.type = type
        self.items = items


class RubricAssessmentProperties:
    id: ContextID
    rubric_id: ContextID
    rubric_association_id: ContextType
    score: ContextType
    artifact_type: FreeFormCriterionComments
    artifact_id: FreeFormCriterionComments
    artifact_attempt: FreeFormCriterionComments
    assessment_type: FreeFormCriterionComments
    assessor_id: FreeFormCriterionComments
    data: Comments
    comments: Comments

    def __init__(self, id: ContextID, rubric_id: ContextID, rubric_association_id: ContextType, score: ContextType, artifact_type: FreeFormCriterionComments, artifact_id: FreeFormCriterionComments, artifact_attempt: FreeFormCriterionComments, assessment_type: FreeFormCriterionComments, assessor_id: FreeFormCriterionComments, data: Comments, comments: Comments) -> None:
        self.id = id
        self.rubric_id = rubric_id
        self.rubric_association_id = rubric_association_id
        self.score = score
        self.artifact_type = artifact_type
        self.artifact_id = artifact_id
        self.artifact_attempt = artifact_attempt
        self.assessment_type = assessment_type
        self.assessor_id = assessor_id
        self.data = data
        self.comments = comments


class RubricAssessment:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricAssessmentProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricAssessmentProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class RubricAssociationProperties:
    id: ContextID
    rubric_id: FreeFormCriterionComments
    association_id: ContextID
    association_type: FreeFormCriterionComments
    use_for_grading: FreeFormCriterionComments
    summary_data: ContextType
    purpose: FreeFormCriterionComments
    hide_score_total: FreeFormCriterionComments
    hide_points: ContextType
    hide_outcome_results: ContextType

    def __init__(self, id: ContextID, rubric_id: FreeFormCriterionComments, association_id: ContextID, association_type: FreeFormCriterionComments, use_for_grading: FreeFormCriterionComments, summary_data: ContextType, purpose: FreeFormCriterionComments, hide_score_total: FreeFormCriterionComments, hide_points: ContextType, hide_outcome_results: ContextType) -> None:
        self.id = id
        self.rubric_id = rubric_id
        self.association_id = association_id
        self.association_type = association_type
        self.use_for_grading = use_for_grading
        self.summary_data = summary_data
        self.purpose = purpose
        self.hide_score_total = hide_score_total
        self.hide_points = hide_points
        self.hide_outcome_results = hide_outcome_results


class RubricAssociation:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricAssociationProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricAssociationProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class RubricCriterionProperties:
    id: FreeFormCriterionComments
    description: Description
    long_description: Description
    points: ContextType
    criterion_use_range: ContextType
    ratings: Assessments

    def __init__(self, id: FreeFormCriterionComments, description: Description, long_description: Description, points: ContextType, criterion_use_range: ContextType, ratings: Assessments) -> None:
        self.id = id
        self.description = description
        self.long_description = long_description
        self.points = points
        self.criterion_use_range = criterion_use_range
        self.ratings = ratings


class RubricCriterion:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: RubricCriterionProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: RubricCriterionProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class RubricRatingProperties:
    id: ContextType
    criterion_id: ContextType
    description: Description
    long_description: Description
    points: ContextType

    def __init__(self, id: ContextType, criterion_id: ContextType, description: Description, long_description: Description, points: ContextType) -> None:
        self.id = id
        self.criterion_id = criterion_id
        self.description = description
        self.long_description = long_description
        self.points = points


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


class Models:
    rubric: Rubric
    rubric_criterion: RubricCriterion
    rubric_rating: RubricRating
    rubric_assessment: RubricAssessment
    rubric_association: RubricAssociation

    def __init__(self, rubric: Rubric, rubric_criterion: RubricCriterion, rubric_rating: RubricRating, rubric_assessment: RubricAssessment, rubric_association: RubricAssociation) -> None:
        self.rubric = rubric
        self.rubric_criterion = rubric_criterion
        self.rubric_rating = rubric_rating
        self.rubric_assessment = rubric_assessment
        self.rubric_association = rubric_association


class Welcome7:
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
