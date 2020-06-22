from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def test_setup(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert("setup test_method tear_down " == self.test.log)


TestCaseTest("test_setup").run()
