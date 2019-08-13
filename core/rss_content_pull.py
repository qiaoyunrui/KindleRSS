# rss 内容拉取和分发
import json

import threadpool
import feedparser

from multiprocessing import cpu_count

rss_source_list = None
pool = threadpool.ThreadPool(cpu_count())


def start(list):
    global rss_source_list
    rss_source_list = list
    _dispatch_pull()


def _dispatch_pull():
    if rss_source_list:
        requests = threadpool.makeRequests(_thread_rss_pull, rss_source_list)
        # 这个表达式很有意思
        [pool.putRequest(req) for req in requests]
        pool.wait()  # 等待所有任务处理完成


def _handle_pull_result(rss_json, rss_source):
    # todo json_handle function 存入数据库，计算差值，生成 html，生成对应格式，发送邮件
    # 还要做好多啊
    # 加油
    print("json\n", len(rss_json), "\nsource\n", rss_source)


# 多线程使用
def _thread_rss_pull(rss_source):
    origin_pull(rss_source, _handle_pull_result)


# 耗时比较严重
def origin_pull(rss_source, handle_closure):
    rss_json = feedparser.parse(rss_source['url'])
    handle_closure(json.dumps(rss_json, ensure_ascii=False), rss_source)
