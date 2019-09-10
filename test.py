import json

import feedparser

d = feedparser.parse('http://www.ruanyifeng.com/blog/atom.xml')

with open("rss.json", "w") as file:
    file.write(json.dumps(d, ensure_ascii=False))
