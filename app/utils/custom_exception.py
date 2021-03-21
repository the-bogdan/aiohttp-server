class ExecutionException(Exception):
    def __init__(self, error: str, message: str, http_code: int = 400):
        super().__init__(error)

        self.error = error
        self.message = message
        self.http_code = http_code
