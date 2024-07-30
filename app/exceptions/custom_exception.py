class CustomException(Exception):
    """
    class for creating custom exception on
    """
    code: int = 404

    def __init__(self, message: str, code):
        super().__init__(message)
        self.code = code
