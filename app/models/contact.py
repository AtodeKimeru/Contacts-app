from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.column(db.String(100))
    email = db.column(db.String(100))
    phone = db.column(db.String(100))

    def __init__(self, fullname, email, phone) -> None:
        self.fullname = fullname
        self.email = email
        self.phone = phone
