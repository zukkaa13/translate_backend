from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.combined_csv_view, name='csv-view'),
    path('add_word/', views.add_word, name='add_word'),
    path("sign/", views.sign, name="sign"),
    path("long/", views.long, name="long"),
    path("login/", views.long, name="login"),  
    path('', views.dashboard, name="home")
]
