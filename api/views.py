from rest_framework import generics
from rest_framework.response import Response
from .models import ShoppingItem
from .serializers import ShoppingItemSerializer
from rest_framework.decorators import api_view

from api import serializers

@api_view(["GET"])
def getData(request):
    items = ShoppingItem.objects.all()
    serializer = ShoppingItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addItem(request):
    serializer = ShoppingItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# class ShoppingItemList(generics.ListCreateAPIView):
#     serializer_class = ShoppingItemSerializer
#     def get_queryset(self):
#         queryset = ShoppingItem.objects.all()
#         name = self.request.querry_parms.get("name")
#         price = self.request.querry_parms.get("price")
#         qrCodeId = self.request.querry_parms.get("qrCodeId")
#         location = self.request.querry_parms.get("location")
#         oldLocations = self.request.querry_parms.get("oldLocations")
#         if name is not None:
#             queryset = queryset.filter(name=name)
#         if price is not None:
#             queryset = queryset.filter(price=price)
#         if qrCodeId is not None:
#             queryset = queryset.filter(qrCodeId=qrCodeId)
#         if location is not None:
#             queryset = queryset.filter(location=location)
#         if oldLocations is not None:
#             queryset = queryset.filter(oldLocations=oldLocations)
#         return Response(queryset)

# class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ShoppingItemSerializer
#     queryset = ShoppingItem.objects.all()