from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('getcats/', views.get_some_cats),
]