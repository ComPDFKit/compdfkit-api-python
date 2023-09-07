class CPDFException(Exception):
    def __init__(self, code=None, message=None, cause=None):
        if message:
            if code:
                super().__init__(message)
                self._code = code
            elif cause:
                super().__init__(message, cause)
            else:
                super().__init__(message)
        elif cause:
            super().__init__(cause)

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code
