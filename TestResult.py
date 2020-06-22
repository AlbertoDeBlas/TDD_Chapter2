class TestResult:

    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count = self.run_count + 1

    def summary(self):
        return "%d run, 0 failed" % self.run_count
