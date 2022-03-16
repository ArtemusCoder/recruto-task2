from django.urls import path

from .views import number

urlpatterns = [
    path('', number, name='number')
]