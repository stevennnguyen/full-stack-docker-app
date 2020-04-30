#from dataclasses import dataclass
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:1234testdb!@sql-server-db:1433/WideWorldImporters?driver=ODBC+Driver+17+for+SQL+Server'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Warehouse Color Class/Model
#@dataclass
class WarehouseColor(db.Model):
    __table_args__ = {'schema':'Warehouse'}
    __tablename__ = 'Colors'

    #id: int
    #data: str

    #id = db.Column('ColorID', db.Integer, primary_key=True)
    #data = db.Column('ColorName', db.String(25))

    id = db.Column('ColorID', db.Integer, primary_key=True)
    color = db.Column('ColorName', db.String(25))
    lasteditedby = db.Column('LastEditedBy', db.Integer)
    #validfrom = db.Column('ValidFrom', db.DateTime, default=datetime.utcnow)
    #validto = db.Column('ValidTo', db.DateTime, default=datetime.utcnow)

    def __init__(self, color, lasteditedby):#, validfrom, validto):
        self.color = color
        self.lasteditedby = lasteditedby
        #self.validfrom = validfrom
        #self.validto = validto

# Warehouse Schema
class WarehouseColorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'color', 'lasteditedby')#, 'validfrom', 'validto')

# Init schema
warehousecolor_schema = WarehouseColorSchema()
warehousecolors_schema = WarehouseColorSchema(many=True)

# Create a Warehouse Color
@app.route('/warehouse/color', methods=['POST'])
def add_color():
    color = request.json['color']
    lasteditedby = request.json['lasteditedby']
    #validfrom = request.json['validfrom']
    #validto = request.json['validto']

    new_color = WarehouseColor(color, lasteditedby)#, validfrom, validto)

    db.session.add(new_color)
    db.session.commit()

    return warehousecolor_schema.jsonify(new_color)

# Get All Warehouse Colors
@app.route('/warehouse/color', methods=['GET'])
def get_color():
    all_colors = WarehouseColor.query.all()
    result = warehousecolors_schema.dump(all_colors)
    return jsonify(result)

@app.route('/')
def index():
    return 'Index Page'

"""
@app.route('/warehouse/colors')
def colors(): 
    return jsonify(WarehouseColor.query.all())

@app.route('/warehouse/colors/<colorid>')
def color(colorid):
    return jsonify(WarehouseColor.query.filter_by(id=colorid).first())
"""

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')