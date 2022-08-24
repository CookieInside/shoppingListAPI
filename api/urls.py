from django.urls import path
#from .views import ShoppingItemList, ShoppingItemDetail
from . import views
urlpatterns = [
#    path("shoppingItem/", ShoppingItemList.as_view()),
#    path("shoppingItem/<int:pk>/", ShoppingItemDetail.as_view()),
    path("get/", views.getData),
    path("post/", views.addItem),
]