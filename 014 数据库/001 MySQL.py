# 连接和操作数据库，我们使用mysqlclient这个第三方库，非常好用的。
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='www',
    passwd='123456',
    db='niushebing',
    charset='utf8'
)
cur = conn.cursor()
cur.execute("select * from article")
rows = cur.fetchall()
print(rows)
cur.close()
conn.commit()
conn.close()
