from wtforms import Form, TextField, SubmitField, validators

class ProductForm(Form):
    product_name = TextField("Product")
    submit = SubmitField("Add")
