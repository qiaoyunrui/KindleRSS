import json
import feedparser

d = feedparser.parse('http://xychen.me/feed')

with open("rss.json", "w") as file:
    file.write(json.dumps(d, ensure_ascii=False))

