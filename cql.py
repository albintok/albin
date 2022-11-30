import pymysql
db=pymysql.connect(host="localhost",user="root",password="albin6431",db="database2")
A=db.cursor()
sql="select * from stud"
A.execute(sql)
row