class ValidationException(Exception):
    """Exception raised for validations.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Salary is not in (5000, 15000) range pobre jeje"):
        self.message = message
        super().__init__(self.message)