
# 调用实例

# 获取全部种类
# Type.getTypeInfo()

# 获取类别名
# Type.getTypeName(typeId)

# 添加类别
# Type.insertName(typeId,typeName)

# 删除类别
# Type.deleteType(typeId)

import pymysql

class Type:

    # 获取全部种类
    def getTypeInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Type"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 获取类别名
    def getTypeName(typeId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT typeName FROM Type WHERE typeId = \""+typeId+"\";";
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            typeName = results[0]
            typeName = typeName[0]
            print(typeName)
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 添加类别
    def insertType(typeId,typeName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO Type(typeId,typeName) VALUES(\""+typeId+"\",\""+typeName+"\");"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

    # 删除类别
    def deleteType(typeId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM Type WHERE typeId = \""+typeId+"\"";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to fetchall userPrefer")

if __name__ == "__main__":
    Type.deleteType("15")