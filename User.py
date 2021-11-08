import pymysql
import json

conn = pymysql.connect(
        host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
        user="root",
        port=25438,
        password="Lcx010327",
        database="Hokkien");

# 创建游标
cursor = conn.cursor();

class User:

    # 获取单个用户信息
    def getUserInfo(userId):
        sql = "SELECT * FROM User WHERE UserId = \"" + userId +"\";";
        try:
            # 执行SQL语句
            cursor.execute(sql),
            # 获取所有记录列表
            results = cursor.fetchall()
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
        sql = "SELECT * FROM User";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 获取所有用户信息
            results = cursor.fetchall()
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
    def insertUserInfo(userId,phoneNumber,userName,profilePicture = '',userMarks = '',userWorks = '',userSearchRecord = '',userPrefer=''):
        sql =  "INSERT INTO User(userId,phoneNumber,userName,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer) \
        VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"% \
        (userId,phoneNumber,userName,profilePicture,userMarks,userWorks,userSearchRecord,userPrefer);
        try:
            # 执行SQL语句
            cursor.execute(sql);
            # 执行sql语句
            conn.commit();
        except:
            print("Error: unable to insert data")


if __name__ == "__main__":
    jsonData = User.getUserInfo()
    print(jsonData)
