from django.urls import path
from .views import soildata_view, form_view, ListView, DetailView

urlpatterns = [
    path('', soildata_view, name='soildata_view'),
    path('add/', form_view, name='form_view'),
    path('api/soildata/', ListView.as_view(), name='soildata_list'),
    path('api/soildata/<int:pk>/', DetailView.as_view(), name='soildata_detail'),
]
