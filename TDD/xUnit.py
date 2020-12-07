

# TestCase
class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
     #       result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
#        print(result.summary())
        self.tearDown()
#        return result


# WasRun
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + " testMethod "

    def setUp(self):
        self.wasRun = None
        self.log = "setUp"

    def tearDown(self):
        self.log = self.log + "tearDown"

    def testBrokenMethod(self):
        raise Exception

# TestResult


class TestResult():
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testFailed(self):
        self.errorCount = self.errorCount + 1

    def testStarted(self):
        self.runCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

# TestSuite


class TestSuite():
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


# TestCaseTest
class TestCaseTest(TestCase):
    def setUp(self):
        result = TestResult()
#        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown" == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))        
        suite.run(self.result)
        print(self.result.summary())
        assert("2 run, 1 failed" == self.result.summary())


TestCaseTest("testSuite").testSuite()
