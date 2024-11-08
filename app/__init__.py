from flask import Flask
from app.db import create_db
from app.routes import main_route, tour_route
from app.data.admin_password import ADMIN_PASSWORD

app = Flask(__name__)
app.secret_key = ADMIN_PASSWORD
app.register_blueprint(main_route)
app.register_blueprint(tour_route)

def main():
    create_db()
    app.run(debug=True)
