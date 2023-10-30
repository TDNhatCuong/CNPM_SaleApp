def load_categories():
    return [
        {
            'id': 1,
            'name': 'Mobie'
        },
        {
            'id': 2,
            'name': 'Talet'
        },
        {
            'id': 3,
            'name': 'LapTop'
        }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Iphone 15',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 2,
        'name': 'Iphone 14',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 3,
        'name': 'Ipad 2022 Pro',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 4,
        'name': 'Ipad 2021',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 5,
        'name': 'Iphone X',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 6,
        'name': 'Iphone 11',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 7,
        'name': 'Iphone 15',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }, {
        'id': 8,
        'name': 'Iphone 15',
        'price': 50000000,
        'img': 'https://img.tgdd.vn/imgt/f_webp,fit_outside,quality_100/https://cdn.tgdd.vn/Products/Images/42/299033/s16/iphone-15-pro-thumbtz-650x650.png'
    }]

    if kw:
        products = [x for x in products if x['name'].find(kw) >= 0]

    return products