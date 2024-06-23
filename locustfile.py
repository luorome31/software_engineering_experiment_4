#! --^-- coding:utf-8 --^--
from locust import HttpUser, task, between, TaskSet
import os
from random import choice
 
# 任务类
 
class TestLogin(TaskSet):
 
    @task
    def to_login(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36", }
 
        data = [{"wd": "qtp"},{"wd": "locust"},{"wd": "java"},{"wd": "loadrunner"}]
 
        res = self.client.get("", params=choice(data), headers=headers)
        print("------",res.status_code)
        print(res.content.decode('utf-8'))
 
 
class WebUser(HttpUser):
    tasks = [TestLogin]
    wait_time = between(2, 5)
    host = "https://www.baidu.com/s"
 
 
if __name__ == '__main__':
    os.system("locust -f locustfile.py")