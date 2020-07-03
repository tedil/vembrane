class VembraneError(Exception):
    """Basic exception for errors raised by vembrane"""

    pass


class UnknownAnnotation(VembraneError):
    """Unknown annotation entry"""

    def __init__(self, record, key, msg=None):
        if msg is None:
            msg = f"No ANN entry for '{key}' in record {record}"
        super(UnknownAnnotation, self).__init__(msg)
        self.record = record
        self.key = key


class UnknownInfoField(VembraneError):
    """Unknown INFO key"""

    def __init__(self, record, field, msg=None):
        if msg is None:
            msg = f"No INFO field '{field}' in record {record}"
        super(UnknownInfoField, self).__init__(msg)
        self.record = record
        self.field = field


class InvalidExpression(VembraneError):
    """Filter expression is invalid"""

    def __init__(self, expression, reason, msg=None):
        if msg is None:
            msg = f"The provided expression '{expression}' is invalid. Reason: {reason}"
        super(InvalidExpression, self).__init__(msg)
        self.expression = expression
