import pymysql

def link_to_database():
    conn = pymysql.connect(
        host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
        user="root",
        port=25438,
        password="Lcx010327",
        database="Hokkien");

    # 创建游标
    cursor = conn.cursor();
    sql = ""
    try:
        cursor.execute(sql)
        cursor.close()
        conn.close()
    except:
        print("Error: unable to fetchall userPrefer")