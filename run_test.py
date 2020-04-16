import unittest
import datetime
from BeautifulReport import BeautifulReport
from common.handle_path import REPORT_DIR
from testcases import test_login

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(test_login))

date = datetime.datetime.now().strftime("%m_%d_%H_%M_%S_")

br = BeautifulReport(suite)
br.report("web自动化测试报告", filename=date + "report.html", report_dir=REPORT_DIR)
