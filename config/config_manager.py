import os
import json

# 从 config.json 中读取配置信息
# kindle_rss config email 123456@qq.com
# kindle_rss config sync_time 0

CONFIG_FILE_NAME = "config.json"

kindle_email = None  # Kindle 邮箱
sync_time = None  # 同步时间 [0-23]


def _init():
    dict = {"kindle_email": "", "sync_time": ""}
    print(dict)
    with open(CONFIG_FILE_NAME, "w") as file:
        file.write(json.dumps(dict))


def _isInit():
    return os.path.exists(CONFIG_FILE_NAME)

def getConfigs():


