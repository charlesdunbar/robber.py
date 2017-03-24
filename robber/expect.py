class expect:
    """
    The main entry point of the library. Most of the time
    you don't have to use anything but this class.

    If you want to register custom matchers, you have to register
    them to `expect`:

    ```
    expect.register(name, klass_that_inherits_from_matchers_base)
    ```

    In order to make the tests more readable, there are a few chains:

    ```
    to, be, a, an, have
    ```
    """
    matchers = {}
    message = None

    def __init__(self, obj):
        self.obj = obj
        self.is_negated = False
        self.__setup_chaining()

    @classmethod
    def fail_with(cls, message):
        cls.message = message

    @classmethod
    def remove_custom_message(cls):
        cls.message = None

    @classmethod
    def register(cls, name, klass):
        cls.matchers[name] = klass

        def method(self, other=None, *args):
            return klass(self.obj, other, self.is_negated, *args).fail_with(self.message).match()

        setattr(cls, name, method)

    @classmethod
    def matcher(cls, name):
        return cls.matchers[name]

    @classmethod
    def unregister(cls, name):
        delattr(cls, name)
        pass

    @classmethod
    def registered(cls, name):
        try:
            getattr(cls, name)
        except AttributeError:
            return False
        else:
            return True

    @property
    def not_to(self):
        self.is_negated = True
        return self

    def __setup_chaining(self):
        self.to = self
        self.be = self
        self.a = self
        self.an = self
        self.have = self
