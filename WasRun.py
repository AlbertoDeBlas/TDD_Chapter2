from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def run(self):
        method = getattr(self, self.name)
        method()

    def test_method(self):
        pass


test = WasRun("test_method")
print(test.wasRun)
test.run()
print(test.wasRun)
