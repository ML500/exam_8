from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from webapp.views.product_views import IndexView, ProductView, ProductCreateView, ProductUpdateVIew, ProductDeleteView
from webapp.views.review_views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView, ReviewView

app_name = 'webapp'
urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateVIew.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/review/add', ReviewCreateView.as_view(),
         name='review_add'),
    path('product/<int:pk>/review/update/', ReviewUpdateView.as_view(),
         name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(),
         name='review_delete'),
    path('review/<int:pk>/', ReviewView.as_view(), name='review_view'),
    ]