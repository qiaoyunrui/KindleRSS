import psycopg2


# 建表
def init():
    # 需要把这些信息存储在本地文件中
    conn = psycopg2.connect(database='kindle_rss', user='postgres', password='postgres', host='localhost', port='5432')
    cur = conn.cursor() # 创建指针对象
    cur.execute("")
    pass
