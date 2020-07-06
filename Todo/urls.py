
from django.urls import path 
from . import views

urlpatterns = [
   # path('',views.start,name='start'),
    #path('index',views.index ,name='index'),
    path('',views.index ,name='index'),
    path('index/add',views.addTodo,name='add'),
    path('index/complete/<Todo_id>',views.completeTodo,name='complete'),
    path('index/deletecompleted',views.deletecompleted,name='deletecompleted'),
    path('index/deleteall',views.deleteall,name='deleteall'),
    path('shortcut',views.shortcut,name='shortcut'),
    path('signup',views.signup_view,name='signup'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
   # path('index/delete',views.delete,name='delete'),
    
]
