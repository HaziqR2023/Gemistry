from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewellery.db'
db = SQLAlchemy(app)

class Jewellery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    base_price = db.Column(db.Float, nullable=False)
    certification_id = db.Column(db.String(50), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/jewellery', methods=['POST'])
def create_jewellery():
    data = request.json
    new_jewellery = Jewellery(
        name=data['name'],
        base_price=data['base_price'],
        certification_id=data.get('certification_id'),
        description=data.get('description')
    )
    db.session.add(new_jewellery)
    db.session.commit()
    return jsonify({'message': 'Jewellery created', 'id': new_jewellery.id}), 201

@app.route('/jewellery/<int:id>', methods=['GET'])
def get_jewellery(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify({
        'id': jewellery.id,
        'name': jewellery.name,
        'base_price': jewellery.base_price,
        'marked_up_price': round(jewellery.base_price * 1.2, 2),
        'certification_id': jewellery.certification_id,
        'description': jewellery.description
    })

@app.route('/jewellery/<int:id>', methods=['PUT'])
def update_jewellery(id):
    jewellery = Jewellery.query.get_or_404(id)
    data = request.json
    if 'name' in data:
        jewellery.name = data['name']
    if 'base_price' in data:
        jewellery.base_price = data['base_price']
    if 'certification_id' in data:
        jewellery.certification_id = data['certification_id']
    if 'description' in data:
        jewellery.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Jewellery updated'})

@app.route('/jewellery/<int:id>', methods=['DELETE'])
def delete_jewellery(id):
    jewellery = Jewellery.query.get_or_404(id)
    db.session.delete(jewellery)
    db.session.commit()
    return jsonify({'message': 'Jewellery deleted'})

@app.route('/jewellery/<int:id>/price', methods=['GET'])
def get_marked_up_price(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify({'marked_up_price': round(jewellery.base_price * 1.2, 2)})

@app.route('/jewellery/<int:id>/certification', methods=['GET'])
def get_certification(id):
    jewellery = Jewellery.query.get_or_404(id)
    return jsonify({'certification_id': jewellery.certification_id})

if __name__ == '__main__':
    app.run(debug=True)