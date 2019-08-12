import json
import sys
import config.config_manager as config_manager
import db.rss_table_manager as rss_table


# d = feedparser.parse('http://xychen.me/feed')

# with open("rss.json", "w") as file:
# file.write(json.dumps(d, ensure_ascii=False))

# config_manager.init()
# rss_table.add_rss_source("李一条", "www.baidu.com")
# rss_table.query_all_rss_source(lambda results: print("@\n", results))

# 这里需要重写一下，有点乱
def handle_commend_params():
    print("参数个数：\t", len(sys.argv))
    print("参数列表：\t", str(sys.argv))
    if len(sys.argv) >= 2:
        if sys.argv[1] == "source":
            print("Source >>>>")
            if len(sys.argv) >= 3:
                if sys.argv[2] == "clear":  # main.py source clear
                    rss_table.clear_rss_source()
                    print("Clear Done")
                    pass
                elif sys.argv[2] == "add":  # main.py source add CSDN www.baidu.com
                    if len(sys.argv) >= 5:
                        rss_table.add_rss_source(sys.argv[3], sys.argv[4])
                        print("Add Done")
                    pass
                elif sys.argv[2] == "remove":  # main.py source remove 1
                    if len(sys.argv) >= 4 and sys.argv[3].isdigit():
                        rss_table.remove_rss_source(sys.argv[3])
                        print("Remove Done")
                    pass
                elif sys.argv[2] == "list":
                    print("RSS Source List:")
                    rss_table.query_all_rss_source(
                        lambda items: [print("id: %s name: %s url: %s" % (item[0], item[1], item[2])) for item in
                                       items])
                    pass
            else:
                print("source 参数错误")
                pass
        else:
            print("开发中")
            pass


if __name__ == "__main__":
    handle_commend_params()
