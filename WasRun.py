from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setup(self):
        self.log = "setup "

    def test_method(self):
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "

#test = WasRun("test_method")
#print(test.wasRun)
#test.run()
#print(test.wasRun)
