from flask import Flask, request, Response
import test

app = Flask(__name__)# 파이썬에서 내장된 특별한 변수로, 현재 모듈의 이름을 나타낸다. 매직 매서드라고도 부르던뎅?

@app.route('/')
def home():
    return 'hello, this is main page!'

@app.route('/about')
def about():
    return 'this is the about page!'


# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.0.1:5000/user/랜덤입력값
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

# 넘버로 진행
@app.route('/number/<int:number>')
def user_number(number):
    return f'Number : {number}'


# post 요청 날리는 법
# (1) postman
# (2) requests
import requests # pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url = url, data = data)
    
    return response

@app.route('/submit', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print('GET method')
        
    if request.method == 'POST':
        print('***POST method***', request.data)    
    return Response('Sucessfully sumbitted', satatus = 200)

if __name__ == '__main__':
    print('__name__ : ', __name__)
    app.run()
    