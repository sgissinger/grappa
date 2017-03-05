from ..operator import Operator


class TrueOperator(Operator):
    """
    Asserts if a given subject is `True` value.

    Example::

        # Should style
        True | should.be.true

        # Should style - negation form
        True | should.not_be.true

        # Expect style
        False | expect.to.be.true

        # Expect style - negation form
        False | expect.to_not.be.true
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('true',)

    # Expected
    expected = 'a "True" boolean value'

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that is "True"',
        'a value that is not "True"',
    )

    def match(self, subject):
        if not self.ctx.negate and not isinstance(subject, bool):
            return False, ['subject is not a bool type']

        return subject is True, []


class FalseOperator(TrueOperator):
    """
    Asserts if a given subject is `False` value.

    Example::

        # Should style
        True | should.be.false

        # Should style - negation form
        True | should.not_be.false

        # Expect style
        False | expect.to.be.false

        # Expect style - negation form
        False | expect.to_not.be.false
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Operator keywords
    operators = ('false',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a value that is "False"',
        'a value that is not "False"',
    )

    # Expected
    expected = 'a "False" boolean value'

    def match(self, subject):
        if not self.ctx.negate and not isinstance(subject, bool):
            return False, ['subject is not a bool type']

        return subject is False, []