from enum import Enum
from typing import Optional, List, Any
from datetime import datetime


class OperationItems:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref


class ItemsType(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    STRING = "string"


class ParameterItems:
    type: ItemsType

    def __init__(self, type: ItemsType) -> None:
        self.type = type


class ParamType(Enum):
    FORM = "form"
    PATH = "path"
    QUERY = "query"


class Parameter:
    param_type: ParamType
    name: str
    description: str
    type: ItemsType
    format: Optional[str]
    required: bool
    deprecated: bool
    enum: Optional[List[str]]
    items: Optional[ParameterItems]

    def __init__(self, param_type: ParamType, name: str, description: str, type: ItemsType, format: Optional[str], required: bool, deprecated: bool, enum: Optional[List[str]], items: Optional[ParameterItems]) -> None:
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


class AllowableValues:
    values: List[str]

    def __init__(self, values: List[str]) -> None:
        self.values = values


class EndAtType(Enum):
    DATETIME = "datetime"
    STRING = "string"


class EndAt:
    description: str
    example: str
    type: EndAtType
    allowable_values: Optional[AllowableValues]

    def __init__(self, description: str, example: str, type: EndAtType, allowable_values: Optional[AllowableValues]) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.allowable_values = allowable_values


class ID:
    description: str
    example: int
    type: ItemsType

    def __init__(self, description: str, example: int, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class AppointmentProperties:
    id: ID
    start_at: EndAt
    end_at: EndAt

    def __init__(self, id: ID, start_at: EndAt, end_at: EndAt) -> None:
        self.id = id
        self.start_at = start_at
        self.end_at = end_at


class Appointment:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: AppointmentProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: AppointmentProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class AllowObserverSignup:
    description: str
    example: bool
    type: ItemsType

    def __init__(self, description: str, example: bool, type: ItemsType) -> None:
        self.description = description
        self.example = example
        self.type = type


class Example:
    id: int
    start_at: datetime
    end_at: datetime

    def __init__(self, id: int, start_at: datetime, end_at: datetime) -> None:
        self.id = id
        self.start_at = start_at
        self.end_at = end_at


class Appointments:
    description: str
    example: List[Example]
    type: ItemsType
    items: OperationItems

    def __init__(self, description: str, example: List[Example], type: ItemsType, items: OperationItems) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.items = items


class ContextCodes:
    description: str
    example: List[str]
    type: ItemsType
    items: ParameterItems

    def __init__(self, description: str, example: List[str], type: ItemsType, items: ParameterItems) -> None:
        self.description = description
        self.example = example
        self.type = type
        self.items = items


class AppointmentGroupProperties:
    id: ID
    title: EndAt
    start_at: EndAt
    end_at: EndAt
    description: EndAt
    location_name: EndAt
    location_address: EndAt
    participant_count: ID
    reserved_times: Appointments
    allow_observer_signup: AllowObserverSignup
    context_codes: ContextCodes
    sub_context_codes: ContextCodes
    workflow_state: EndAt
    requiring_action: AllowObserverSignup
    appointments_count: ID
    appointments: Appointments
    new_appointments: Appointments
    max_appointments_per_participant: ID
    min_appointments_per_participant: ID
    participants_per_appointment: ID
    participant_visibility: EndAt
    participant_type: EndAt
    url: EndAt
    html_url: EndAt
    created_at: EndAt
    updated_at: EndAt

    def __init__(self, id: ID, title: EndAt, start_at: EndAt, end_at: EndAt, description: EndAt, location_name: EndAt, location_address: EndAt, participant_count: ID, reserved_times: Appointments, allow_observer_signup: AllowObserverSignup, context_codes: ContextCodes, sub_context_codes: ContextCodes, workflow_state: EndAt, requiring_action: AllowObserverSignup, appointments_count: ID, appointments: Appointments, new_appointments: Appointments, max_appointments_per_participant: ID, min_appointments_per_participant: ID, participants_per_appointment: ID, participant_visibility: EndAt, participant_type: EndAt, url: EndAt, html_url: EndAt, created_at: EndAt, updated_at: EndAt) -> None:
        self.id = id
        self.title = title
        self.start_at = start_at
        self.end_at = end_at
        self.description = description
        self.location_name = location_name
        self.location_address = location_address
        self.participant_count = participant_count
        self.reserved_times = reserved_times
        self.allow_observer_signup = allow_observer_signup
        self.context_codes = context_codes
        self.sub_context_codes = sub_context_codes
        self.workflow_state = workflow_state
        self.requiring_action = requiring_action
        self.appointments_count = appointments_count
        self.appointments = appointments
        self.new_appointments = new_appointments
        self.max_appointments_per_participant = max_appointments_per_participant
        self.min_appointments_per_participant = min_appointments_per_participant
        self.participants_per_appointment = participants_per_appointment
        self.participant_visibility = participant_visibility
        self.participant_type = participant_type
        self.url = url
        self.html_url = html_url
        self.created_at = created_at
        self.updated_at = updated_at


class AppointmentGroup:
    id: str
    description: str
    required: List[Any]
    deprecated: bool
    deprecation_description: None
    properties: AppointmentGroupProperties

    def __init__(self, id: str, description: str, required: List[Any], deprecated: bool, deprecation_description: None, properties: AppointmentGroupProperties) -> None:
        self.id = id
        self.description = description
        self.required = required
        self.deprecated = deprecated
        self.deprecation_description = deprecation_description
        self.properties = properties


class Models:
    appointment: Appointment
    appointment_group: AppointmentGroup

    def __init__(self, appointment: Appointment, appointment_group: AppointmentGroup) -> None:
        self.appointment = appointment
        self.appointment_group = appointment_group


class Welcome6:
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
