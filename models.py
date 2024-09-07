from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ticker_symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
