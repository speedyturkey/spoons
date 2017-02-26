from application import db

class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Users(Base):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    requests = db.relationship('Requests', backref='user',
                                lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)


class Products(Base):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(128))
    requests = db.relationship('Requests', backref='product',
                                lazy='dynamic')

    def __repr__(self):
        return '<Product {}>'.format(self.product_name)

class Requests(Base):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    requested_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #TODO add __repr__ method using requestor and product name or maybe date.
