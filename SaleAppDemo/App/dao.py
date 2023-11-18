from App.models import Category, Product, User
import hashlib
from App import app


def load_categories():
    return  Category.query.all()
    # return [
    #     {
    #         'id': 1,
    #         'name': 'Mobie'
    #     },
    #     {
    #         'id': 2,
    #         'name': 'Talet'
    #     },
    #     {
    #         'id': 3,
    #         'name': 'LapTop'
    #     }]


def load_products(kw=None, cate_id=None, page=None):
    # products = [{
    #     'id': 1,
    #     'name': 'Iphone 15',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 2,
    #     'name': 'Iphone 14',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 3,
    #     'name': 'Ipad 2022 Pro',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 4,
    #     'name': 'Ipad 2021',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 5,
    #     'name': 'Iphone X',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 6,
    #     'name': 'Iphone 11',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 7,
    #     'name': 'Iphone 15',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }, {
    #     'id': 8,
    #     'name': 'Iphone 15',
    #     'price': 50000000,
    #     'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    # }]
    #
    # if kw:
    #     products = [x for x in products if x['name'].find(kw) >= 0]
    #
    # return products
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()


def count_product():
    return Product.query.count()

def get_user_by_id(id):
    return User.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                            User.password.__eq__(password)).first()