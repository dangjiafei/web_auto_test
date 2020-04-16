"""测试数据的保存。

接口自动化自动化测试放在 Excel 当中，
web 自动化测试数据：1， py 文件当中，  2， Excel 当中

数据分组：把不同的测试用例方法需要用到的数据放入不同的组
分组的依据：是因为测试步骤不一样。

# 1 通过表单
# 2 接口当中也是有数据分组，不同的表单当中，

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
