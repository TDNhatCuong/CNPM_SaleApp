from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose, AdminIndexView
from App import app, db, dao
from App.models import Category, Product, UserRoleEnum
from flask_login import logout_user, current_user
from flask import redirect, request


class MyAdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', stats=dao.count_products_by_cate())


admin = Admin(app=app, name="QUẢN TRỊ CỬA HÀNG", template_mode="bootstrap4", index_view=MyAdminIndex())


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class AuthenticatedAdmin1(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthenticatedAdmin2(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyProductView(AuthenticatedAdmin1):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']       #Tìm kiếm theo 'name'
    column_filters = ['price', 'name']      #Lọc theo
    can_export = True                       #Xuất file excel
    can_view_details = True                 #Xem chi tiết


class MyCategoryView(AuthenticatedAdmin1):
    column_list = ['name', 'products']



class MyStatsView(AuthenticatedAdmin2):
    @expose('/')
    def index(self):
        kw = request.args.get("kw")
        return self.render('admin/stats.html',
                           stats=dao.revenue_stats(kw),
                           month_stats = dao.revenue_stats_by_month())

class MyLogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(MyLogoutView(name='Đăng xuất'))