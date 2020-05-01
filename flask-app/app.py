from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Init app
app = Flask(__name__)
# Local database
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:1234testdb!@sql-server-db:1433/WideWorldImporters?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Warehouse Color Class/Model
class WarehouseColor(db.Model):
    # Database
    __table_args__ = {'schema':'Warehouse'}
    __tablename__ = 'Colors'

    id = db.Column('ColorID', db.Integer, primary_key=True)
    color = db.Column('ColorName', db.String(25))
    lasteditedby = db.Column('LastEditedBy', db.Integer)

    def __init__(self, color, lasteditedby):
        self.color = color
        self.lasteditedby = lasteditedby

# Warehouse Schema
class WarehouseColorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'color', 'lasteditedby')

# Init schema
warehousecolor_schema = WarehouseColorSchema()
warehousecolors_schema = WarehouseColorSchema(many=True)

# Create a Warehouse Color
@app.route('/warehouse/color', methods=['POST'])
def add_color():
    color = request.json['color']
    lasteditedby = request.json['lasteditedby']

    new_color = WarehouseColor(color, lasteditedby)

    db.session.add(new_color)
    db.session.commit()

    return warehousecolor_schema.jsonify(new_color)

# Get All Warehouse Colors
@app.route('/warehouse/color', methods=['GET'])
def get_colors():
    all_colors = WarehouseColor.query.all()
    result = warehousecolors_schema.dump(all_colors)
    return jsonify(result)

# Get Single Warehouse Color
@app.route('/warehouse/color/<id>', methods=['GET'])
def get_color(id):
    color = WarehouseColor.query.get(id)
    return warehousecolor_schema.jsonify(color)

# Update a Product
@app.route('/warehouse/color/<id>', methods=['PUT'])
def update_color(id):
    warehousecolor = WarehouseColor.query.get(id)

    color = request.json['color']
    lasteditedby = request.json['lasteditedby']

    warehousecolor.color = color
    warehousecolor.lasteditedby = lasteditedby

    db.session.commit()

    return warehousecolor_schema.jsonify(warehousecolor)

# Delete Warehouse Color
@app.route('/warehouse/color/<id>', methods=['DELETE'])
def delete_color(id):
    color = WarehouseColor.query.get(id)
    db.session.delete(color)
    db.session.commit()
    return warehousecolor_schema.jsonify(color)

@app.route('/')
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')