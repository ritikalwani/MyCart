
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ConatctUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('productview/<int:myid>', views.productView, name="ProductView"),
    path('search/', views.search, name="Search"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="handlerequest")
]
