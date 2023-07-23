from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api = Api(app)
api.add_resource(HelloWorld, '/api')

@app.route('/healthz')
def health_check():
    try:
        db.session.query("1").first()
    except Exception as e:
        print(e)
        return "Not Healthy", 500
    else:
        return "Healthy", 200

db.create_all()  # Create tables for our models

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
