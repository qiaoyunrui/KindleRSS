# rss 内容拉取和分发
import json

import threadpool
import feedparser

from multiprocessing import cpu_count

rss_source_list = None
pool = threadpool.ThreadPool(cpu_count())


def start():
    _dispatch_pull()


def set_rss_source_list(origin_list):
    global rss_source_list
    rss_source_list = origin_list


def _dispatch_pull():
    if rss_source_list:
        requests = threadpool.makeRequests(_thread_rss_pull, rss_source_list)
        # 这个表达式很有意思
        [pool.putRequest(req) for req in requests]
        pool.poll()  # 等待所有任务处理完成


def handle_pull_result(rss_json):
    print(rss_json)


# 多线程使用
def _thread_rss_pull(rss_url):
    # todo json_handle function 存入数据库，计算差值，生成 html，生成对应格式，发送邮件
    # 还要做好多啊
    # 加油
    origin_pull(rss_url, handle_pull_result)


# 耗时比较严重
def origin_pull(rss_url, handle_closure):
    rss_json = feedparser.parse(rss_url)
    handle_closure(json.dumps(rss_json, ensure_ascii=False))
