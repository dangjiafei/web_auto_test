import os
import unittest
import datetime
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_path import REPORT_DIR, CASE_DIR

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

date = datetime.datetime.now().strftime("%m_%d_%H_%M_%S_")

runner = HTMLTestRunner(stream=open(os.path.join(REPORT_DIR, date + "report.html"), "wb"),
                        title="Web自动化测试报告",
                        description="------",
                        tester="党佳飞"
                        )
runner.run(suite)
