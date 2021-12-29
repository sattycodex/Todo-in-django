from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<id>/', views.delete, name="delete"),
    path('Unmark_as_complete/<id>/', views.Unmark_as_complete, name="Unmark_as_complete"),
    path('mark_as_complete/<id>/', views.mark_as_complete, name="mark_as_complete"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
]