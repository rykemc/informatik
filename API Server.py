# 1. Import necessary packages
import os
import json
import socket
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 2. Initialize Flask app
app = Flask(__name__)

# 3. Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 4. Define SQLAlchemy Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(200))
    ip_address = db.Column(db.String(100))
    contents = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Order {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# 5. Create the API endpoint (Route)
@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()
        ip_address = request.remote_addr

        # Create a new Order object
        new_order = Order(
            device_name=order_data.get('device_name'),
            ip_address=ip_address,
            contents=json.dumps(order_data.get('contents'))
        )

        # Add the new order to the database
        db.session.add(new_order)
        db.session.commit()

        return jsonify({'message': 'Order sent successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Error processing order', 'error': str(e)}), 500

# 6. Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)

 
