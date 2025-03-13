from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/Listing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Listing Model
class Listing(db.Model):
    __tablename__ = 'listing'

    ListingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ListingOwner = db.Column(db.Integer, nullable=False)
    ListingName = db.Column(db.String(255), nullable=False)
    ListingCategory = db.Column(db.String(255), nullable=False)
    ListingPrice = db.Column(db.Float, nullable=False)
    ListingItem = db.Column(db.Float, nullable=False)
    ListingDesc = db.Column(db.String(500))
    isActive = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "ListingID": self.ListingID,
            "ListingOwner": self.ListingOwner,
            "ListingName": self.ListingName,
            "ListingCategory": self.ListingCategory,
            "ListingPrice": self.ListingPrice,
            "ListingItem": self.ListingItem,
            "ListingDesc": self.ListingDesc,
            "isActive": self.isActive
        }

# @app.route('/')
# def home():
#     return "Welcome to the Listings Microservice"

# Route to create a new listing (POST)
@app.route('/listing', methods=['POST'])
def create_listing():
    data = request.json
    new_listing = Listing(
        ListingOwner=data['ListingOwner'],
        ListingName=data['ListingName'],
        ListingCategory=data['ListingCategory'],
        ListingPrice=data['ListingPrice'],
        ListingItem=data['ListingItem'],
        ListingDesc=data.get('ListingDesc', ''),
        isActive=data.get('isActive', True)
    )
    
    db.session.add(new_listing)
    db.session.commit()

    return jsonify({"message": "Listing created", "ListingID": new_listing.ListingID}), 201

# Route to retrieve all listings (GET)
@app.route('/listing', methods=['GET'])
def get_listings():
    listings = Listing.query.filter_by(isActive=True).all()
    return jsonify([listing.to_dict() for listing in listings])

# Route to retrieve a specific listing by ID (GET)
@app.route('/listing/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing:
        return jsonify(listing.to_dict())
    return jsonify({"message": "Listing not found"}), 404

# Route to update a listing (PUT)
@app.route('/listing/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if not listing:
        return jsonify({"message": "Listing not found"}), 404

    data = request.json
    listing.ListingName = data['ListingName']
    listing.ListingCategory = data['ListingCategory']
    listing.ListingPrice = data['ListingPrice']
    listing.ListingItem = data['ListingItem']
    listing.ListingDesc = data.get('ListingDesc', listing.ListingDesc)
    listing.isActive = data.get('isActive', listing.isActive)

    db.session.commit()
    return jsonify({"message": "Listing updated"}), 200

# Route to delete a listing (DELETE)
@app.route('/listing/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if not listing:
        return jsonify({"message": "Listing not found"}), 404

    db.session.delete(listing)
    db.session.commit()

    return jsonify({"message": "Listing deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)