class ExecutionException(Exception):
    """
    This exception handles by error_handler_middleware layer and after that
    returns Response with correct status code and json body with error and message inside to user
    """
    def __init__(self, error: str, message: str, http_code: int = 400):
        super().__init__(error)

        self.error = error
        self.message = message
        self.http_code = http_code
