from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.combined_csv_view, name='csv-view'),
    path('add_word/', views.add_word, name='add_word'),
    path("sign/", views.sign, name="sign"),
    path("long/", views.long, name="long"),
    path("login/", views.long, name="login"), 
    path("Aone", views.Aone, name="Aone"), 
    path("Atwo", views.Atwo, name="Atwo"), 
    path("Btwo", views.Btwo, name="Btwo"),
    path("Cone", views.Cone, name="Cone"),  
    path('', views.dashboard, name="home"), 
]
