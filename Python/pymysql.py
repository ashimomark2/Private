import pymysql

conn = pymysql.connect(host='localhost',user='root',password='z8aSWUTBMySQL',db='tripadvisor',charset='utf8mb4')

with conn.cursor() as cursor:
    cursor.execute("select distinct spot_id from tag")
    spotids = cursor.fetchall()

    for id in spotids:
        print(id)