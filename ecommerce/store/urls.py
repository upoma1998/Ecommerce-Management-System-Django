from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('storelog/', views.storelog, name="storelog"),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]
