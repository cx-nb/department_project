# 导包
import requests


# 创建要封装的员工类
class DepartmentApi:
    def __init__(self):
        # 定义员工模块的URL
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    def add_dep(self, depname, depcode,magname,intoinfo,headers):
        # 根据外部传入的username和mobile拼接成要发送的请求体数据
        jsonData = {"name":depname,
                    "code":depcode,
                    "manager":magname,
                    "introduce":intoinfo,
                    "pid":"1066238836272664576"
                    }
        # 发送添加员工请求，并返回结果
        return requests.post(url=self.dep_url, json=jsonData, headers=headers)

    def query_dep(self, dep_id, headers):
        # 拼接查询员工的URL
        query_url = self.dep_url + "/" + dep_id
        # 发送查询员工的接口请求，并return返回结果
        return requests.get(url=query_url, headers=headers)

    def modify_dep(self, dep_id,depname,depcode,headers):
        # 拼接修改员工的URL
        modify_url = self.dep_url + "/" + dep_id
        jsonData = {"name": depname,
                    "code": depcode,
                    }
        # 发送修改员工的接口请求，并 return返回结果
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    def delete_dep(self, dep_id, headers):
        # 拼接删除员工的URL
        delete_url = self.dep_url + "/" + dep_id
        # 发送删除员工的接口请求，return返回数据
        return requests.delete(url=delete_url, headers=headers)