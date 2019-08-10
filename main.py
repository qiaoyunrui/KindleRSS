import json
import feedparser
import config.config_manager as config_manager
import db.rss_table_manager as rss_table

# d = feedparser.parse('http://xychen.me/feed')

# with open("rss.json", "w") as file:
    # file.write(json.dumps(d, ensure_ascii=False))

# config_manager.init()
rss_table.add_rss_source("李一条", "www.baidu.com")
