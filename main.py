import json
import feedparser
import config.config_manager as config_manager

d = feedparser.parse('http://xychen.me/feed')

with open("rss.json", "w") as file:
    file.write(json.dumps(d, ensure_ascii=False))

config_manager._init()