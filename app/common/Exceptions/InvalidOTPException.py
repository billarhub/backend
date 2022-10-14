class InvalidOTPException(Exception):
    """Exception raised for validations.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="OTP inválido"):
        self.message = message
        super().__init__(self.message)