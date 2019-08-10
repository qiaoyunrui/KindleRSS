import db.db_manager as db_manager

if not db_manager.is_init():
    db_manager.init()


def add_rss_source(name, url):
    sql = "INSERT INTO rss_list (name, url, updated) VALUES ('%s', '%s', '');" % (name, url)
    print(sql)
    db_manager.do(lambda cursor: cursor.execute(sql))
