from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/genei', methods=['GET'])
def show_genei():
    chart = list(db.genei.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'genei_chart': chart, 'msg':'지니차트연결됫움'})

# @app.route('/api/bugs', methods=['GET'])
# def show_bugs():
#     chart = list(db.bugs.find({}, {'_id': False}))
#     return jsonify({'result': 'success', 'bugs_chart': chart})
#
# @app.route('/api/melon', methods=['GET'])
# def show_melon():
#     chart = list(db.melon.find({}, {'_id': False}))
#     return jsonify({'result': 'success', 'melon_chart': chart})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)