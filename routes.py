from flask import Blueprint, request, jsonify
from models import Stock, db

stock_bp = Blueprint('stock_bp', __name__)

# Get all stocks
@stock_bp.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = Stock.query.all()
    stock_list = [{"id": stock.id, "name": stock.name, "ticker_symbol": stock.ticker_symbol, "price": stock.price} for stock in stocks]
    return jsonify(stock_list)

# Get a single stock by id
@stock_bp.route('/stocks/<int:id>', methods=['GET'])
def get_stock(id):
    stock = Stock.query.get_or_404(id)
    return jsonify({"id": stock.id, "name": stock.name, "ticker_symbol": stock.ticker_symbol, "price": stock.price})

# Add a new stock
@stock_bp.route('/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    new_stock = Stock(name=data['name'], ticker_symbol=data['ticker_symbol'], price=data['price'])
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({"message": "Stock added successfully"}), 201

# Update a stock by id
@stock_bp.route('/stocks/<int:id>', methods=['PUT'])
def update_stock(id):
    stock = Stock.query.get_or_404(id)
    data = request.get_json()
    stock.name = data['name']
    stock.ticker_symbol = data['ticker_symbol']
    stock.price = data['price']
    db.session.commit()
    return jsonify({"message": "Stock updated successfully"})

# Delete a stock by id
@stock_bp.route('/stocks/<int:id>', methods=['DELETE'])
def delete_stock(id):
    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    return jsonify({"message": "Stock deleted successfully"})


