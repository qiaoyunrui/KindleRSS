# rss 内容拉取和分发
import json

import threadpool
import feedparser
import db.rss_table_manager as rss_table
import db.rss_content_table_manager as content_table

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


def _handle_pull_result(rss_content, rss_source):
    # todo json_handle function 存入数据库，计算差值，生成 html，生成对应格式，发送邮件
    # 还要做好多啊
    # 加油
    # print("json\n", len(rss_content), "\nsource\n", rss_source)
    _store_rss_content(rss_content, rss_source)
    # if rss_content['updated'] == rss_source['updated']:
    #     print("[%s] 没有更新。" % (rss_source['name']))
    # else:  # 数据更新了
    #     print("[%s] 更新了。" % (rss_source['name']))
    #     rss_source['updated'] = rss_content['updated']
    #     rss_table.update_rss_source(rss_source)
    #     _store_rss_content(rss_content, rss_source)


# 存储 rss 内容
def _store_rss_content(rss_content, rss_source):
    content_table.add_contents(rss_content['entries'], rss_source)


# 正文生成 HTML
def _generate_html(entry):
    pass


# 生成 Kindle 支持的文本
def _generate_kindle_file(html):
    pass


# 向 Kindle 发送邮件
def _send_email(file_path):
    pass


# 多线程使用
def _thread_rss_pull(rss_source):
    origin_pull(rss_source, _handle_pull_result)


# 耗时比较严重
def origin_pull(rss_source, handle_closure):
    rss_content = feedparser.parse(rss_source['url'])
    # handle_closure(json.dumps(rss_json, ensure_ascii=False), rss_source)
    handle_closure(rss_content, rss_source)
