from flask import Flask, request, render_template, Response
from flask_cors import CORS
import jsonpickle
from DBManager import DBManager
from InputValidators import InputValidators

DBPATH = ''

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print('Post request.')

        print("Starting processing...")
        response = {'response': 'hi'}
        response_pickled = jsonpickle.encode(response)
        return Response(response=response_pickled, status=200, mimetype="application/json")

    return render_template("python_index.html")

# if __name__ == '__main__':
#     app.secret_key = 'super secret key'
#     app.config['SESSION_TYPE'] = 'filesystem'
#     app.run(host='172.20.1.45', port=5019)











