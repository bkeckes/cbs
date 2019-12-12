from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Transfer(Resource):
    def get(self):
        return {
            'transfer': ['Apfel', 'Birne', 'Zitrone', 'Test', 'Zwiebel', 'DD']
        }
api.add_resource(Transfer, '/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
