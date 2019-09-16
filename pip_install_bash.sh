# 需要安装的仓库
echo "HelloWorld"
# shellcheck disable=SC2034
libs=(threadpool feedparser psycopg2 pdfkit)
# shellcheck disable=SC2068
pip3 install ${libs[@]}

# pdfkit 需要的依赖
apt-get install wkhtmltopdf