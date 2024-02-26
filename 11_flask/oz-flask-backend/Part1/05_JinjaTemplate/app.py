from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title' : 'Flask Jinja Template',
        'user' : 'zidol',
        'is_admin' : True,
        'item_list' : ["Item1", "Item2", "Item3"]
    }
    
    # (1) rendering 할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data = data)

# 과제
@app.route('/homework')
def index():
    users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
    ]

    return render_template('homework.html', users = users)

    


if __name__ == '__main__':
    app.run(debug = True) # debug=True를 넣으면 서버를 껏다 켜지 않아도 바로 반영된다!