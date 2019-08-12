import db.db_manager as db_manager

if not db_manager.is_init():
    db_manager.init()


# 添加 rss 源
def add_rss_source(name, url):
    sql = "INSERT INTO rss_list (name, url, updated) VALUES ('%s', '%s', '');" % (name, url)
    print(sql)
    db_manager.do(lambda cursor: cursor.execute(sql))


# 获取所有 rss 源
def query_all_rss_source(result_closure):
    sql = "SELECT * FROM rss_list;"
    print(sql)
    db_manager.query(lambda cursor: cursor.execute(sql),
                     result_closure)


def remove_rss_source(id):
    sql = "DELETE FROM rss_list WHERE id = %s;" % id
    print(sql)
    db_manager.do(lambda cursor: cursor.execute(sql))


def clear_rss_source():
    db_manager.do(lambda cursor: cursor.execute("DELETE FROM rss_list;"))
