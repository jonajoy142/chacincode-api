class DBNotFoundException(Exception):
    """
    class for creating custom exception on
    """
    code: int = 404

    def __init__(self, message, code=404):
        super().__init__(message)
        self.code = code
