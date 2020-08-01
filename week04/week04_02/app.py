from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']

    document = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    }

    db.orders.insert_one(document)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    orders = list(db.orders.find({},{"_id": False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)