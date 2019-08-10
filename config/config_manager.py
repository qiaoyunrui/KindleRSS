import os
import json

# 从 config.json 中读取配置信息
# kindle_rss config email 123456@qq.com
# kindle_rss config sync_time 0

CONFIG_FILE_NAME = "config.json"

kindle_email = None  # Kindle 邮箱
sync_time = 0  # 同步时间 [0-23]


# 从文件中读取配置
def init():
    global kindle_email, sync_time
    with open(CONFIG_FILE_NAME, "r") as file:
        json_str = file.read()
        if json_str:
            config = json.loads(json_str)
            kindle_email = config['kindle_email']
            sync_time = config['sync_time']


def getSyncTime():
    return sync_time


def getKindleEmail():
    return kindle_email


def setConfig(_kindle_email=None, _sync_time=0):
    global kindle_email, sync_time
    kindle_email = _kindle_email
    sync_time = _sync_time
