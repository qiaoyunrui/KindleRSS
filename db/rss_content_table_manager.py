import db.db_manager as db_manager
import os

if not db_manager.is_init():
    db_manager.init()


def sync_exist(id):
    sql = "SELECT count(id) FROM rss_content WHERE id = '%s';" % (id)
    cursor = db_manager.conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def add_contents(content_list, rss_source):
    if content_list and rss_source:
        source_id = rss_source['id']
        new_content_list = filter(lambda content: sync_exist(content['id'])[0][0] == 0, content_list)
        if not new_content_list:
            pass
        pre_sql = "INSERT INTO rss_content(id, source_id, author, title, summary, updated, link, content) VALUES "
        content_sql_list = []
        [content_sql_list.append("('%s', %s, '%s', '%s', '%s', '%s', '%s', '%s')" %
                                 (item['id'], source_id, item['author'], item['title'],
                                  item['summary'], item['updated'],
                                  item['link'], item['content'][0]['value'].replace("\'", "\'\'"))) for item in
         new_content_list]
        # print(pre_sql + ",".join(content_sql_list) + ";")
        if not content_sql_list:
            print("没有更新")
            return
        # 字符串转移
        sql = "%s%s;" % (pre_sql, ",".join(content_sql_list))
        with open("insert.sql", "w") as file:
            temp_sql = sql
            file.write(temp_sql)
        db_manager.do(lambda cursor: cursor.execute(sql))
