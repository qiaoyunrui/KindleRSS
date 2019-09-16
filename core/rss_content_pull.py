# rss 内容拉取和分发
import json

import threadpool
import feedparser
import db.rss_content_table_manager as content_table
import os
import pdfkit
import time

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
    new_content_list = _store_rss_content(rss_content, rss_source)
    if not new_content_list:  # 没有更新的文章
        return
    html_list = []
    [html_list.append(_generate_html(content)) for content in new_content_list]
    pdf_file_list = []
    [pdf_file_list.append(_generate_pdf(html)) for html in html_list]

    # todo 生成 pdf
    # todo 发送邮件
    # 先不删除 html
    # 单独线程执行
    # if rss_content['updated'] == rss_source['updated']:
    #     print("[%s] 没有更新。" % (rss_source['name']))
    # else:  # 数据更新了
    #     print("[%s] 更新了。" % (rss_source['name']))
    #     rss_source['updated'] = rss_content['updated']
    #     rss_table.update_rss_source(rss_source)
    #     _store_rss_content(rss_content, rss_source)


# 存储 rss 内容
def _store_rss_content(rss_content, rss_source):
    return content_table.add_contents(rss_content['entries'], rss_source)


# 正文生成 HTML
# 返回文件路径
def _generate_html(entry):
    html = "<!DOCTYPE html><html lang=\"en\"><head><meta " \
           "charset=\"UTF-8\"><title>%s</title></head><body>%s</body></html>" % (
               entry['title'], entry['content'][0]['value'])
    if not os.path.exists("./html"):
        os.mkdir("./html")
    file_name = "./html/%s.html" % (entry['title'])
    with open(file_name, "w") as file:
        file.write(html)
        print("[Generate] ", file_name)
    return [file_name, entry['title']]


# 生成 pdf
# 返回文件路径
def _generate_pdf(html):
    if not os.path.exists("./pdf"):
        os.mkdir("./pdf")
    pdf_file_name = "./pdf/%s.pdf" % (html[1])
    # 生成 PDF 文件
    pdfkit.from_file(html[0], pdf_file_name)
    print("[Generate] ", pdf_file_name)
    return pdf_file_name


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
