from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import uuid  # Importing the uuid module to generate unique certification IDs

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/Jewellery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Jewellery(db.Model):
    __tablename__ = 'Jewellery'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    item_number = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    certification_id = db.Column(db.String(50), unique=True, nullable=True)  # Added certification_id column

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'marked_up_price': round(self.price * 1.2, 2),
            'item_number': self.item_number,
            'description': self.description,
            'is_active': self.is_active,
            'certification_id': self.certification_id  # Return certification_id in the dictionary
        }

with app.app_context():
    db.create_all()

@app.route('/jewellery', methods=['POST'])
def create_jewellery():
    data = request.json
    
    # Generate a unique certification ID
    certification_id = str(uuid.uuid4())  # Using uuid4 to generate a unique certification ID
    
    new_jewellery = Jewellery(
        name=data['JewelleryName'],
        category=data['JewelleryCategory'],
        price=data['JewelleryPrice'],
        item_number=data['JewelleryItem'],
        description=data.get('JewelleryDesc'),
        is_active=data.get('isActive', True),
        certification_id=certification_id  # Assign the generated certification ID
    )
    
    db.session.add(new_jewellery)
    db.session.commit()
    return jsonify({'message': 'Jewellery created', 'id': new_jewellery.id, 'certification_id': certification_id}), 201

@app.route('/jewellery', methods=['GET'])
def get_all_jewellery():
    jewellery_list = Jewellery.query.all()
    return jsonify([j.to_dict() for j in jewellery_list])

@app.route('/jewellery/<int:id>', methods=['GET'])
def get_jewellery(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify(jewellery.to_dict())

@app.route('/jewellery/<int:id>', methods=['PUT'])
def update_jewellery(id):
    # jewellery = Jewellery.query.get_or_404(id)
    # data = request.json
    # jewellery.name = data.get('JewelleryName', jewellery.name)
    # jewellery.category = data.get('JewelleryCategory', jewellery.category)
    # jewellery.price = data.get('JewelleryPrice', jewellery.price)
    # jewellery.item_number = data.get('JewelleryItem', jewellery.item_number)
    # jewellery.description = data.get('JewelleryDesc', jewellery.description)
    # jewellery.is_active = data.get('isActive', jewellery.is_active)
    # db.session.commit()
    # return jsonify({'message': 'Jewellery updated'})

    jewellery = Jewellery.query.get_or_404(id)  # Retrieve the item by ID
    data = request.json

    # Update only the fields that are passed in the request
    jewellery.name = data.get('JewelleryName', jewellery.name)
    jewellery.category = data.get('JewelleryCategory', jewellery.category)
    jewellery.price = data.get('JewelleryPrice', jewellery.price)
    jewellery.item_number = data.get('JewelleryItem', jewellery.item_number)
    jewellery.description = data.get('JewelleryDesc', jewellery.description)
    jewellery.is_active = data.get('isActive', jewellery.is_active)

    # Commit the transaction to save changes in the database
    try:
        db.session.commit()
        return jsonify({'message': 'Jewellery updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating jewellery', 'error': str(e)}), 500


@app.route('/jewellery/<int:id>', methods=['DELETE'])
def delete_jewellery(id):
    jewellery = Jewellery.query.get_or_404(id)
    db.session.delete(jewellery)
    db.session.commit()
    return jsonify({'message': 'Jewellery deleted'})

@app.route('/jewellery/<int:id>/price', methods=['GET'])
def get_marked_up_price(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify({'marked_up_price': round(jewellery.price * 1.2, 2)})

@app.route('/jewellery/<int:id>/certification', methods=['GET'])
def get_certification(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify({'certification_id': jewellery.certification_id})

if __name__ == '__main__':
    app.run(debug=True)