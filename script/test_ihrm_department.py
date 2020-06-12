# 导包
import unittest, logging


import app
from parameterized import parameterized

# 创建测试类
from api.department import DepartmentApi
from api.login import LoginApi
from utils import assert_common, read_dep_data


class TestIHRMEmployeeParams(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.dep_api = DepartmentApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type":"application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 定义员工模块的文件路径
    dep_filepath = app.BASE_DIR + "/data/dep_data.json"
    # 参数化
    @parameterized.expand(read_dep_data(dep_filepath, 'add_dep'))
    def test02_add_dep(self,depname1, depcode1,magname1,intoinfo1,success,code,message,http_code):
        logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        # 发送添加员工的接口请求
        response = self.dep_api.add_dep(depname1,depcode1,magname1,intoinfo1,app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        # 提取员工中的令牌并把员工令牌保存到全局变量中
        app.DEP_ID = response.json().get("data").get("id")
        # 打印保存的员工ID
        logging.info("保存到全局变量的员工的ID为：{}".format(app.DEP_ID))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, "query_dep"))
    def test03_query_dep(self,success,code,message,http_code):
        # 发送查询员工的接口请求:
        response = self.dep_api.query_dep(app.DEP_ID, app.HEADERS)
        # 打印查询员工的数据
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, "modify_dep"))
    def test04_modify_dep(self,depname2, depcode2,success,code,message,http_code):
        # 调用封装的修改员工接口，发送接口请求
        response = self.dep_api.modify_dep(app.DEP_ID,depname2, depcode2,app.HEADERS)
        # 打印数据
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, "delete_dep"))
    def test05_delete_dep(self,success,code,message,http_code):
        # 调用封装的删除员工接口哦，发送接口请求
        response = self.dep_api.delete_dep(app.DEP_ID, app.HEADERS)
        # 打印删除员工的结果为
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)
