from django.contrib import admin
from django.urls import path

from .views import inicio, home, list_car, listing, listing_edit, like_listing_view

urlpatterns = [
    path('', inicio, name='main'),
    path('home/', home, name='home'),
    path('list_car/', list_car, name='list_car'),
    path('listing/<str:id>/', listing, name='listing'),
    path('listing/<str:id>/edit', listing_edit, name='listing_edit'),
    path('listing/<str:id>/like', like_listing_view, name='like_listing')
]
