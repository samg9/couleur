from flask import Flask, jsonify,request
from scraper.scraper import get_profile,scrape
app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def hwello_world():
    return 'Hello, World!'


@app.route('/col/api/v0/col', methods=['GET'])
def get_tasks():
    user = request.args.get('user')
    print("user is ", user)
    temp = get_profile(user)
    print("result0:",temp)
    print(jsonify({'user': user}))
    return jsonify({'tasks': tasks})