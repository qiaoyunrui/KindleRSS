# 需要安装的仓库
echo "HelloWorld"
# shellcheck disable=SC2034
libs=(threadpool feedparser psycopg2,)
# shellcheck disable=SC2068
pip3 install ${libs[@]}
