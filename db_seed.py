from application import db, models

u1 = models.Users(first_name='First', last_name='User', email='first.user@spoons.online')
u2 = models.Users(first_name='Second', last_name='User', email='second.user@spoons.online')
u3 = models.Users(first_name='Third', last_name='User', email='third.user@spoons.online')

p1 = models.Products(product_name='Spoons')
p2 = models.Products(product_name='Forks')
p3 = models.Products(product_name='Knives')

r1 = models.Requests(requested_by=u1, product=p1)
r2 = models.Requests(requested_by=u2, product=p2)
r3 = models.Requests(requested_by=u3, product=p3)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(r1)
db.session.add(r2)
db.session.add(r3)
db.session.commit()
