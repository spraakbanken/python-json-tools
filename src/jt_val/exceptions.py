from json_tools import exceptions


class JsonValidatorException(exceptions.JsonToolsException):
    """
    Base exception for json_tools.val
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

        super().__init__(message)


class SchemaDefinitionException(JsonValidatorException):
    def __init__(self, message):
        super().__init__(message)


class ValidationException(JsonValidatorException):
    def __init__(self, message):
        super().__init__(message)
