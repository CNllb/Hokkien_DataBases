# 使用样例

# 查找单个用户的信息
# User.getUserInfo(userId)

# 查找全部用户信息
# User.getUserInfo()

# 插入用户信息
# User.insertUserInfo(userId,phoneNumber,userName,profilePicture = '',userMarks = '',
# userWorks = '',userSearchRecord = '',userPrefer=''):

# 更换用户头像
# User.updateprofilePicture(userId,newProfilePicture)

# 更换用户名
# User.updateUserName(userId,newUserName)

# 更换用户手机号码
# User.updatephoneNumber(userId,newphoneNumber)

import pymysql
import json

class User:

    # 获取单个用户信息
    def getSingleUserInfo(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql = "SELECT * FROM User WHERE UserId = \"" + userId +"\";";
        try:
            # 执行SQL语句
            cursor.execute(sql),
            # 获取所有记录列表
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            print(results)
            jsonData = []
            for row in results:
                result = {}
                result['userId'] = row[0]
                result['phoneNumber'] = row[1]
                result['userName'] = row[2]
                result['profileName'] = row[3]
                result['userMarks'] = row[4]
                result['userWorks'] = row[5]
                result['userSearchRecord'] = row[6]
                result['userPrefer'] = row[7]
                print
                u'转换为列表字典的原始数据：', jsonData
                jsonData.append(result)
        except:
            print("Error: unable to fetch single userInfo")
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 获取所有用户信息
    def getUserInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM User";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 获取所有用户信息
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result['userId'] = row[0]
                result['phoneNumber'] = row[1]
                result['userName'] = row[2]
                result['profileName'] = row[3]
                result['userMarks'] = row[4]
                result['userWorks'] = row[5]
                result['userSearchRecord'] = row[6]
                result['userPrefer'] = row[7]
                print
                u'转换为列表字典的原始数据：', jsonData
                jsonData.append(result)
        except:
            print("Error: unable to fetch single userInfo")
        else:
            jsondatar = json.dumps(jsonData, ensure_ascii=False)
            return jsondatar[1:len(jsondatar) - 1]

    # 插入用户信息
    def insertUserInfo(userId,phoneNumber,userName,profilePicture = '',userMarks = None,userWorks = None,userSearchRecord = None,userPrefer=None):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql =  "INSERT INTO User(userId,phoneNumber,userName,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer) \
        VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"% \
        (userId,phoneNumber,userName,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer);
        try:
            # 执行SQL语句
            cursor.execute(sql);
            # 执行sql语句
            conn.commit();
            cursor.close()
            conn.close()
        except:
            print("Error: unable to insert data")

    # 更换用户头像
    def updateprofilePicture(userId,newProfilePicture):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET profilePicture = \"" + newProfilePicture + "\" WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行mysql语句
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to update profilePicture")

    # 更换用户名
    def updateUserName(userId,newUserName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE User SET userName = \""+newUserName+"\""+"WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
            cursor.close()
            conn.close()
        except:
            print("Error: unable to update userName")

    # 更换用户手机号码
    def updatephoneNumber(userId,newphoneNumber):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();

        sql = "UPDATE User SET phoneNumber = \""+newphoneNumber+"\""+" WHERE userId = \"" + userId + "\";";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
        except:
            print("Error: unable to update phoneNumber")
        cursor.close()
        conn.close()

    # 查找用户收藏记录
    def getuserMarks(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT userMarks FROM User WHERE userId = \""+userId+"\";";

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for row in result:
                userMarks = row[0]
            userMarks = userMarks.split(",")
            if userMarks[0] == '':
                return []
            return userMarks
        except:
            print("Error: unable to fetch userMarks")

    # 添加用户收藏记录
    def insertuserMarks(userId,workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql_fetch = "SELECT userMarks FROM User WHERE userId = \""+userId+"\";";
        try:
            cursor.execute(sql_fetch)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for row in result:
                userMarks = row[0]
            userMarks = userMarks.split(",")
            print(len(result))
            userMarks.append(workId)
            print(userMarks)
        except:
            print("Error: unable to update userMarks")

if __name__ == "__main__":
    User.insertuserMarks("7","1615")
