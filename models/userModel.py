from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'sexsler'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad = db.Column(db.String(100), nullable=False)
    soyad = db.Column(db.String(100), nullable=False)
    ata_adi = db.Column(db.String(100), nullable=False)
    fin_kod = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    faculty_id = db.Column(db.Integer)
    faculty_name = db.Column(db.Text)
    kafedra_id = db.Column(db.Integer)
    kafedra_name = db.Column(db.Text)
    vezife_id = db.Column(db.Integer)
    vezife_name = db.Column(db.Text)
    icrayamesulsexs_id = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'ad': self.ad,
            'soyad': self.soyad,
            'ata_adi': self.ata_adi,
            'fin_kod': self.fin_kod,
            'faculty_id': self.faculty_id,
            'faculty_name': self.faculty_name,
            'kafedra_id': self.kafedra_id,
            'kafedra_name': self.kafedra_name,
            'vezife_id': self.vezife_id,
            'vezife_name': self.vezife_name,
            'icrayamesulsexs_id': self.icrayamesulsexs_id
        }