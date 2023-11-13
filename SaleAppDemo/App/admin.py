from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from App import app, db
from App.models import Category, Product



admin = Admin(app=app, name="QUẢN TRỊ CỬA HÀNG", template_mode="bootstrap4")

class MyProductView(ModelView):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']       #Tìm kiếm theo 'name'
    column_filters = ['price', 'name']      #Lọc theo
    can_export = True                       #Xuất file excel
    can_view_details = True                 #Xem chi tiết


class MyCategoryView(ModelView):
    column_list = ['name', 'products']



class MyStatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))