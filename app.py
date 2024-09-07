from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from models import db  # Import db from models.py
from routes import stock_bp  # Import routes after initializing db
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)
# Configurations
app.config.from_object('config.Config')

# Database setup
db.init_app(app)  # Initialize db
migrate = Migrate(app, db)

# Register the blueprint
app.register_blueprint(stock_bp)

if __name__ == '__main__':
    app.run(debug=True)
