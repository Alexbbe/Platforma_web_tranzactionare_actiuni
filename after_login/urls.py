from django.contrib import admin
from django.urls import path
from after_login import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('index', views.index, name='index'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('user_info', views.user_info, name='user_info'),
    path('company', views.company_page, name='company'),
    path('portofolio', views.portofolio, name='portofolio'),
    path('marketnews', views.market_news, name='marketnews'),
    path('portofolio/transactions/<str:company>', views.tran,name='transactions'),
    path('portofolio/transactions/delete/<str:company>/<int:id>',views.delete_transaction, name='delete'),
    path('add_company',views.add_company,name='add_company'),
    path('del_company',views.del_company,name='del_company')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)