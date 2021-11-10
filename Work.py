# 调用实例

#

import pymysql

class Work:

    # 获取全部作品
    def getWorkInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 添加作品信息
    def insertWork(workId,workName,workContent,workType = ""):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO Work(workId,workName,workContent,workType) VALUES (" \
              "\""+workId+"\",\""+workName+"\",\""+workContent+"\",\""+workType+"\");"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

if __name__ == "__main__":
    Work.insertWork("12","第一个信息","信息内容")