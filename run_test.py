import pytest
import datetime

date = datetime.datetime.now().strftime("%m_%d_%H_%M_%S_")

if __name__ == '__main__':
    pytest.main([r"--alluredir=logs/allure_report/"])
    # pytest.main([r'--html=reports\{}report.html'.format(date)])
    # '-m login' 标记
    # --reruns 2 失败之后再运行两次,  --reruns-delay 5 失败之后间隔5秒在运行
