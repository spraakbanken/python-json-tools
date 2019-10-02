from sb_json_tools import exceptions


class JsonValidatorException(exceptions.JsonToolsException):
    """
    Base exception for json_tools.val
    """


class SchemaDefinitionException(JsonValidatorException):
    pass


class ValidationException(JsonValidatorException):
    pass
