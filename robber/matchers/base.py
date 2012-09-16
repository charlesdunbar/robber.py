from robber.bad_expectation import BadExpectation

"""
Base matcher. All matchers inherit from it.
If you want to create a custom matcher, it's a good
idea to extend it, as well.
"""
class Base:
    def __init__(self, actual, expected = None, *args):
        self.actual = actual
        self.expected = expected
        self.args = args

    def match(self):
        if not self.matches():
            raise BadExpectation, self.failure_message()
