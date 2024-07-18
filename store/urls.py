from django.urls import path
from . import views
from category.models import Category


urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='discs_by_category'),
    path('<slug:category_slug>/<slug:disc_slug>/', views.disc_detail, name='disc_detail')
]
