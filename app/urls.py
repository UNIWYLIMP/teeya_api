from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_contact', views.create_contact, name='create_contact'),
    path('create_booking', views.create_booking, name='create_booking'),
]

# path('properties/<str:text>/',views.viewProperty,name='viewProperty'),
"""
    new_contact us
    new_booking
"""