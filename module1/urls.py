from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name="home"),
    path('addt',views.add_template,name="add_template"),
    path('add',views.addition,name="addition"),
    path('register',views.register_template,name="register_template"),
    path('login',views.login,name='login'),
    path('success',views.success,name='success'),
    path('rec',views.record,name='record'),
    path('samp',views.sample,name='sample'),
    path('recd',views.recorddata,name='recorddata')
]