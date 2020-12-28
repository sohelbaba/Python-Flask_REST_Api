from config import db
from App import app

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


#deploy link rest-api
#https://stores-python-flask-api.herokuapp.com/items