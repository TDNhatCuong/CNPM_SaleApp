import hashlib
from App import db
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default='https://toppng.com/uploads/preview/roger-berry-avatar-placeholder-11562991561rbrfzlng6h.png')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):          #Ghi đè category (khóa ngọai)
        return self.name


class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    img = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == "__main__":
    from App import app
    with app.app_context():
        #db.create_all()
        import hashlib

        u1 = User(name='UserNC',
                  username='nhatcuong',
                  password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                  user_role=UserRoleEnum.USER)

        u2 = User(name='AdminNC',
                  username='cuongnhat',
                  password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                  user_role=UserRoleEnum.ADMIN)

        db.session.add_all([u1, u2])
        db.session.commit()

        import hashlib

        u = User(name='Admin',
                 username='admin',
                 password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)

        db.session.add(u)
        db.session.commit()

        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')

        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        p1 = Product(name='Ipad pro 2022', price=25000000, category_id=2,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")
        p2 = Product(name='Iphone 15', price=29000000, category_id=1,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")
        p3 = Product(name='Iphone 13', price=19000000, category_id=1,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")
        p4 = Product(name='Ipad mini 6', price=14000000, category_id=2,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")
        p5 = Product(name='Samsung S23 Ultra', price=22000000, category_id=1,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")
        p6 = Product(name='Samsung Tab S9', price=18000000, category_id=2,
                     img="https://cdn.kalvo.com/uploads/img/gallery/55251-apple-iphone-15-pro-max-2.jpg")

        db.session.add_all([p1, p2, p3, p4, p5, p6])
        db.session.commit()

