import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )

cursor = connection.cursor()

sql = 'SELECT * FROM customers'
cursor.execute(sql)

customers = cursor.fetchone()
print('customers : ', customers)
print('customers : ', customers['id'])
print('customers : ', customers['customerName'])
print('customers : ', customers['contry'])
