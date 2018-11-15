

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


class JsonValidatorSchemaDefinitionException(JsonValidatorException):
    def __init__(self, message):
        super(JsonValidatorSchemaDefinitionException, self).__init__(message)


class JsonValidatorValidationException(JsonValidatorException):
    def __init__(self, message):
        super(JsonValidatorValidationException, self).__init__(message)
