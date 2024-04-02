import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='0000',
                             db='classicmodels',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # 커서 생성
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        sql = "YOUR_SQL_QUERY"
        cursor.execute(sql)

        # 결과 받아오기
        result = cursor.fetchall()
        print(result)

finally:
    # 데이터베이스 연결 종료
    connection.close()