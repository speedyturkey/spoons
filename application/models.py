from application import db
from datetime import datetime

class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)


class Users(Base):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    role = db.Column(db.String(128))

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)


class Products(Base):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128), nullable=False)
    requests = db.relationship('Requests', backref='product',
                                lazy='dynamic')

    def __repr__(self):
        return '<Product {}>'.format(self.product_name)

class Requests(Base):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    requested_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    requested_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(128))
    requestor_note = db.Column(db.String(255))
    reviewed_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    requested_by = db.relationship("Users", foreign_keys=[requested_by_id])
    reviewed_by = db.relationship("Users", foreign_keys=[reviewed_by_id])

    #TODO add __repr__ method using requestor and product name or maybe date.
