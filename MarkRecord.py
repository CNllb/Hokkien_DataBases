# coding = utf-8
# 调用实例

# 获取全部收藏记录
# MarkRecord.getMarkRecord()

# 获取某个作品的收藏人数
# MarkRecord.getMarkRecordCount(workId)

# 获取某个用户的收藏作品数量
# MarkRecord.getSingleMarkRecordCount(userId)

# 插入收藏记录
# MarkRecord.insertMarkRecord(markRecord,userId,workId)

# 删除收藏记录
# MarkRecord.deleteMarkRecord(userId,workId)

# 查看某个用户的收藏记录
# MarkRecord.getSingleMarkRecords(userId)

import pymysql
import json

class MarkRecord:

    # 获取全部收藏记录
    def getMarkRecord():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM MarkRecord"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["markRecord"] = row[2]
                result["userId"] = row[0]
                result["workId"] = row[1]
                jsonData.append(result)
            return jsonData
        except:
            return False

    # 获取某个作品的收藏人数
    def getMarkRecordCount(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT COUNT(*) FROM MarkRecord WHERE workId = \""+workId+"\""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            results = results[0]
            return results
        except:
            return False

    # 获取某个用户的收藏作品数量
    def getSingleMarkRecordCount(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT COUNT(*) FROM MarkRecord WHERE userId = \""+userId+"\""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            result = results[0]
            result = result[0]
            return result
        except:
            print("Error: unable to fetchall userPrefer")

    # 获取某个用户的收藏记录
    def getSingleMarkRecords(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM MarkRecord WHERE userId = \""+userId+"\""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["markRecord"] = row[2]
                result["userId"] = row[0]
                result["workId"] = row[1]
                jsonData.append(result)
            return jsonData
        except:
            return False

    # 插入收藏记录
    def insertMarkRecord(userId,workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO MarkRecord(userId,workId) \
        VALUES('%s','%s')"% \
        (userId,workId);
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = MarkRecord.getMarkRecord()
            return results
        except:
            return False

    # 删除收藏记录
    def deleteMarkRecord(userId,workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM MarkRecord WHERE userId = \""+userId+"\" AND workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = MarkRecord.getMarkRecord()
            return results
        except:
            return False