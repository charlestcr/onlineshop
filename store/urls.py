from django.urls import path
from .views import cart,store,checkout,updateItem,processOrder
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
  path('login/',views.CustomLoginView.as_view(),name='login'),
  path('logout/',LogoutView.as_view(next_page='store'),name='logout'),
  path('register/',views.RegisterPage.as_view(),name='register'),
  path('',store,name='store'),
  path('cart/',cart,name='cart'),
  path('checkout/',checkout,name='checkout'),
  path('update_item/',updateItem,name='update_item'),
  path('process_order/',processOrder,name='process_order')


]