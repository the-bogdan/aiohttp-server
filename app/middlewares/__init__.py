from .auth_middleware import auth_middleware
from .session_middleware import session_middleware
from .error_handler_middleware import error_handler_middleware


middleware_list = [
    error_handler_middleware,
    session_middleware,
    auth_middleware
]
