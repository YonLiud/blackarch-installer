import sys

from enum import IntEnum

if sys.version_info >= (3, 5):
    class HTTPStatus(IntEnum):

        def __init__(self, *a) -> None: ...

        phrase: str
        description: str

        CONTINUE = ...
        SWITCHING_PROTOCOLS = ...
        PROCESSING = ...
        OK = ...
        CREATED = ...
        ACCEPTED = ...
        NON_AUTHORITATIVE_INFORMATION = ...
        NO_CONTENT = ...
        RESET_CONTENT = ...
        PARTIAL_CONTENT = ...
        MULTI_STATUS = ...
        ALREADY_REPORTED = ...
        IM_USED = ...
        MULTIPLE_CHOICES = ...
        MOVED_PERMANENTLY = ...
        FOUND = ...
        SEE_OTHER = ...
        NOT_MODIFIED = ...
        USE_PROXY = ...
        TEMPORARY_REDIRECT = ...
        PERMANENT_REDIRECT = ...
        BAD_REQUEST = ...
        UNAUTHORIZED = ...
        PAYMENT_REQUIRED = ...
        FORBIDDEN = ...
        NOT_FOUND = ...
        METHOD_NOT_ALLOWED = ...
        NOT_ACCEPTABLE = ...
        PROXY_AUTHENTICATION_REQUIRED = ...
        REQUEST_TIMEOUT = ...
        CONFLICT = ...
        GONE = ...
        LENGTH_REQUIRED = ...
        PRECONDITION_FAILED = ...
        REQUEST_ENTITY_TOO_LARGE = ...
        REQUEST_URI_TOO_LONG = ...
        UNSUPPORTED_MEDIA_TYPE = ...
        REQUESTED_RANGE_NOT_SATISFIABLE = ...
        EXPECTATION_FAILED = ...
        UNPROCESSABLE_ENTITY = ...
        LOCKED = ...
        FAILED_DEPENDENCY = ...
        UPGRADE_REQUIRED = ...
        PRECONDITION_REQUIRED = ...
        TOO_MANY_REQUESTS = ...
        REQUEST_HEADER_FIELDS_TOO_LARGE = ...
        INTERNAL_SERVER_ERROR = ...
        NOT_IMPLEMENTED = ...
        BAD_GATEWAY = ...
        SERVICE_UNAVAILABLE = ...
        GATEWAY_TIMEOUT = ...
        HTTP_VERSION_NOT_SUPPORTED = ...
        VARIANT_ALSO_NEGOTIATES = ...
        INSUFFICIENT_STORAGE = ...
        LOOP_DETECTED = ...
        NOT_EXTENDED = ...
        NETWORK_AUTHENTICATION_REQUIRED = ...
