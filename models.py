from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    doctor = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=True)  # New field for message
