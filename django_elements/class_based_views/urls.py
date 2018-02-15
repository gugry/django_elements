from django.urls import path

from .views import Base_View, Form_View

urlpatterns = [
    path('base_view/', Base_View.as_view(), name='base_view'),
    path('form_view/', Form_View.as_view(), name='form_view'),
]
