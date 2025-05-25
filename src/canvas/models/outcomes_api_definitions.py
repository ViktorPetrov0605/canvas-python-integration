from enum import Enum
from typing import Optional, List, Any


class OperationItems:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref


class ParameterItems:
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
    items: Optional[ParameterItems]
    enum: Optional[List[str]]

    def __init__(self, param_type: ParamType, name: str, description: str, type: str, format: Optional[str], required: bool, deprecated: bool, items: Optional[ParameterItems], enum: Optional[List[str]]) -> None:
        self.param_type = param_type
        self.name = name
        self.description = description
        self.type = type
        self.format = format
        self.required = required
        self.deprecated = deprecated
        self.items = items
        self.enum = enum


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
    items: Optional[OperationItems]

    def __init__(self, method: str, summary: str, notes: str, nickname: str, parameters: List[Parameter], response_fields: List[Any], deprecated: bool, deprecation_description: str, type: str, items: Optional[OperationItems]) -> None:
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


class Assessed:
    description: str
    example: bool
    type: str

    def __init__(self, description: str, example: bool, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class CalculationInt:
    description: str
    example: int
    type: str

    def __init__(self, description: str, example: int, type: str) -> None:
        self.description = description
        self.example = example
        self.type = type


class AllowableValues:
    values: List[str]

    def __init__(self, values: List[str]) -> None:
        self.values = values


class CalculationMethod:
    description: str
    example: str
    type: str
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: str, type: str, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.allowable_values = allowable_values


class ContextType:
    example: str
    type: str

    def __init__(self, example: str, type: str) -> None:
        self.example = example
        self.type = type


class Ratings:
    description: str
    type: str
    items: OperationItems

    def __init__(self, description: str, type: str, items: OperationItems) -> None:
        self.description = description
        self.type = type
        self.items = items


class OutcomeProperties:
    id: CalculationInt
    url: CalculationMethod
    context_id: CalculationInt
    context_type: ContextType
    title: CalculationMethod
    display_name: CalculationMethod
    description: CalculationMethod
    vendor_guid: CalculationMethod
    points_possible: CalculationInt
    mastery_points: CalculationInt
    calculation_method: CalculationMethod
    calculation_int: CalculationInt
    ratings: Ratings
    can_edit: Assessed
    can_unlink: Assessed
    assessed: Assessed
    has_updateable_rubrics: Assessed

    def __init__(self, id: CalculationInt, url: CalculationMethod, context_id: CalculationInt, context_type: ContextType, title: CalculationMethod, display_name: CalculationMethod, description: CalculationMethod, vendor_guid: CalculationMethod, points_possible: CalculationInt, mastery_points: CalculationInt, calculation_method: CalculationMethod, calculation_int: CalculationInt, ratings: Ratings, can_edit: Assessed, can_unlink: Assessed, assessed: Assessed, has_updateable_rubrics: Assessed) -> None:
        self.id = id
        self.url = url
        self.context_id = context_id
        self.context_type = context_type
        self.title = title
        self.display_name = display_name
        self.description = description
        self.vendor_guid = vendor_guid
        self.points_possible = points_possible
        self.mastery_points = mastery_points
        self.calculation_method = calculation_method
        self.calculation_int = calculation_int
        self.ratings = ratings
        self.can_edit = can_edit
        self.can_unlink = can_unlink
        self.assessed = assessed
        self.has_updateable_rubrics = has_updateable_rubrics


class Outcome:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: OutcomeProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: OutcomeProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class OutcomeAlignmentProperties:
    id: CalculationInt
    assignment_id: CalculationInt
    assessment_id: CalculationInt
    submission_types: CalculationMethod
    url: CalculationMethod
    title: CalculationMethod

    def __init__(self, id: CalculationInt, assignment_id: CalculationInt, assessment_id: CalculationInt, submission_types: CalculationMethod, url: CalculationMethod, title: CalculationMethod) -> None:
        self.id = id
        self.assignment_id = assignment_id
        self.assessment_id = assessment_id
        self.submission_types = submission_types
        self.url = url
        self.title = title


class OutcomeAlignment:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: OutcomeAlignmentProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: OutcomeAlignmentProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    outcome: Outcome
    outcome_alignment: OutcomeAlignment

    def __init__(self, outcome: Outcome, outcome_alignment: OutcomeAlignment) -> None:
        self.outcome = outcome
        self.outcome_alignment = outcome_alignment


class Welcome5:
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
