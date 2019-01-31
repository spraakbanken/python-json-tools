

class JsonValidatorException(Exception):
    """
    Base exception for json_validator
    """

    def __init__(self, message):
        """
        A short description.

        A bit longer description.

            :param message: description

        Returns:
            type: description

        Raises:
            Exception: description

        """

        super(JsonValidatorException, self).__init__(message)


class SchemaDefinitionException(JsonValidatorException):
    def __init__(self, message):
        super(SchemaDefinitionException, self).__init__(message)


class ValidationException(JsonValidatorException):
    def __init__(self, message):
        super(ValidationException, self).__init__(message)
