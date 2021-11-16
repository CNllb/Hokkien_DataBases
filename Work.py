# 调用实例

# 添加作品信息
# Work.insertWork(workId,workName,workContent,workType = "")

# 获取单个作品信息
# Work.getSingleWorkInfo(workId)

# 获取全部作品信息
# Work.getWorkInfo()

# 更新作品名称
# Work.updateWorkName(workId,newWorkName)

# 更新作品内容
# Work.updateWorkContent(workId,newWorkContent)

# 更新作品分类
# Work.updateWorkType(workId,newWorkType)

# 删除作品信息
# Work.deleteWork(workId)

import pymysql

class Work:

    # 获取单个作品信息
    def getSingleWorkInfo(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work WHERE WorkId = \"" + workId + "\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

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
              "'"+workId+"','"+workName+"','"+workContent+"','"+workType+"');"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 更改作品名称
    def updateWorkName(workId,newWorkName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workName = \""+newWorkName+"\" WHERE workId = \""+workId+"\";";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 更改作品内容
    def updateWorkContent(workId,newWorkContent):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workContent = \""+newWorkContent+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 更改作品分类
    def updateWorkType(workId,newWorkType):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workType = \""+newWorkType+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 删除作品
    def deleteWork(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM Work WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

if __name__ == "__main__":
    Work.insertWork("6","AboutBin","66666","1515")