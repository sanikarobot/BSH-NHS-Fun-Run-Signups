class CustomException(Exception):
    """
    Built to handle custom exceptions better. This helps differentiate exceptions between ones that we create and ones
    that Python throws in order to prevent us from making major mistakes.
    This class inherits from Exception and provides the same functionality.
    """
    def __init__(self, message):
        super().__init__(message)

