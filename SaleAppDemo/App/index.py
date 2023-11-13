from flask import render_template, request
import dao
from App import app, login


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw=kw)

    return render_template("index.html", categories=cates, products=products)

@app.route('/products/<id>')
def details(id):
    return render_template("details.html")


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    request.form.get('username')
    request.form.get('password')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


#Chạy server
if __name__ == "__main__":
    from App import admin
    app.run(debug=None)