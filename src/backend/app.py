from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
"mysql+pymysql://root:root123@localhost/calculator_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Calculation(db.Model):
    __tablename__ = "calculations"
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Float)
    b = db.Column(db.Float)
    operation = db.Column(db.String(5))
    result = db.Column(db.String(50))

@app.route("/", methods=["POST"])
def calculate():
    a = float(request.form["a"])
    b = float(request.form["b"])
    op = request.form["op"]

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = "Error" if b == 0 else a / b

    row = Calculation(a=a, b=b, operation=op, result=str(result))
    db.session.add(row)
    db.session.commit()

    return str(result)

app.run(host="0.0.0.0", port=5000)
