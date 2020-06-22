from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def test_setup(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert("setup test_method tear_down " == self.test.log)

    def test_result(self):
        self.test = WasRun("test_method")
        result = self.test.run()
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert("1 run, 1 failed", result.summary)


TestCaseTest("test_setup").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result").run()
