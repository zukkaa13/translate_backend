from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.combined_csv_view, name='csv-view'),
    path('add_word/', views.add_word, name='add_word'),
    path('', views.dashboard)
]
