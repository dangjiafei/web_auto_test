"""
测试数据的保存
数据分组：把不同的测试用例方法需要用到的数据放入不同的组
分组的依据：测试步骤不一样
"""

login_data_error = [
    {"mobile": "", "pwd": "", "expected": "请输入手机号"},
    {"mobile": "18675467432", "pwd": "", "expected": "请输入密码"},
]

login_data_invalid = [
    {"mobile": "18745678943", "pwd": "12", "expected": "此账号没有经过授权，请联系管理员!"},
]

login_data_success = [
    {"mobile": "18684720553", "pwd": "python", "expected": "我的帐户[华华]"},
]
