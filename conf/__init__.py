"""配置文件ini, yaml, py文件  constant.py"""
import os


class Setting:
    # host 地址
    host = 'http://120.78.128.25:8765'

    # root_path 项目的根目录
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # img_path, 截图目录 img
    img_path = os.path.join(root_path, 'screenshot')
    if not os.path.exists(img_path):
        os.mkdir(img_path)
