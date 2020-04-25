from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:1234testdb!@sql-server-db:1433/WideWorldImporters?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

@dataclass
class WarehouseColor(db.Model):
    __table_args__ = {'schema':'Warehouse'}
    __tablename__ = 'Colors'

    id: int
    data: str

    id = db.Column('ColorID', db.Integer, primary_key=True)
    data = db.Column('ColorName', db.String(25))

@app.route('/')
def index():
    return 'Index Page'

@app.route('/warehouse/colors')
def colors(): 
    return jsonify(WarehouseColor.query.all())

@app.route('/warehouse/colors/<colorid>')
def color(colorid):
    return jsonify(WarehouseColor.query.filter_by(id=colorid).first())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')