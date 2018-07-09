from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():
    if (request.methods == 'POST'):
        some_json = request.get_json()
        return jsonify({"you sent": some_json}), 201

     else:
         return jsonify({"about": "Hello World! Gesuka RESTful here.."})


app.route('/multi/<int:num>', methods = ['GET'])


def get_multiply10(num):
    return jsnonify({'result': num * 10})


if __name__ =='__main__':
    app.run(debug=True)