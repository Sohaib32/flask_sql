from flask import Flask
from models.models import db
from routes.routes import routes_app

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///docs.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sohaib123@localhost/docs'
app.register_blueprint(routes_app)

# Initialize the database with the app context
with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)