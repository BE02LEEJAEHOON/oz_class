from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect (
	host = '127.0.0.1',
    user = 'root',
    password = '0000',
    db='musinsa',
    charset='utf8mb4'
)

cur = db.cursor()
sql = "SELECT * FROM musinsa"
cur.execute(sql)

musinsa_data = cur.fetchall()
# print(musinsa_data)

@app.route('/')
def index():
	return render_template('admin.html', data_list = musinsa_data)


if __name__ == '__main__':
	app.debug = True
	app.run