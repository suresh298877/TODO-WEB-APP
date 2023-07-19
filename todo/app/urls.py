from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("login/",views.login,name='login'),
    path("logout/",views.logoutUser,name='logoutUser'),
    path("signup/",views.signup,name='signup'),
    path("add-todo/",views.todo,name='todo'),
    path("delete_todo/<int:id>",views.delete_todo,name='delete_todo'),
    path("change_status/<int:id>/<str:status>",views.change_todo,name='change_status'),

    # path('ghome/',views.ghome,name='ghome'),
    # path("homee/",views.homee,name='homee'),
    path("gverify/<slug:token>",views.gverify,name='verify'),
    
]