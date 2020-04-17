import pytest
import unittest
import datetime
# from library.HTMLTestRunnerNew import HTMLTestRunner
# from common.handle_path import REPORT_DIR, CASE_DIR

# suite = unittest.TestSuite()

loader = unittest.TestLoader()
# suite.addTest(loader.discover(CASE_DIR))

date = datetime.datetime.now().strftime("%m_%d_%H_%M_%S_")

# runner = HTMLTestRunner(stream=open(os.path.join(REPORT_DIR, date + "report.html"), "wb"),
#                         title="Web自动化测试报告",
#                         description="------",
#                         tester="党佳飞"
#                         )
# runner.run(suite)


if __name__ == '__main__':
    pytest.main([r'--html=reports\{}report.html'.format(date)])
    # '-m login' 标记
    # --reruns 2 失败之后再运行两次,  --reruns-delay 5 失败之后间隔5秒在运行
