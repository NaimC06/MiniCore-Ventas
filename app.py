
from flask import Flask
from flask_migrate import Migrate
from utils.database import db
from pathlib import Path
import os
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{DB_PATH.as_posix()}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY", "dev"
)

db.init_app(app)
migrate = Migrate(app, db)

from controllers.venta_controller import main_blueprint
app.register_blueprint(main_blueprint)

def init_db():
    if not DB_PATH.exists():
        with sqlite3.connect(DB_PATH) as conn:
            with open(
                BASE_DIR / "data.sql",
                encoding="utf-8"
            ) as archivo:
                conn.executescript(archivo.read())

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
