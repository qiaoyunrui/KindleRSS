import json
import pdfkit
import feedparser

# d = feedparser.parse('http://www.ruanyifeng.com/blog/atom.xml')
#
# with open("rss.json", "w") as file:
#     file.write(json.dumps(d, ensure_ascii=False))

pdfkit.from_file('./html/3964727530290340566.html', "demo.pdf")
