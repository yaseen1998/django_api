from django.shortcuts import render
from rest_framework import generics
from .serializer import AddSerializer
from .models import Add_data
# Create your views here.

class AddListView(generics.ListCreateAPIView):
    serializer_class = AddSerializer
    queryset = Add_data.objects.all()

class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddSerializer
    queryset = Add_data.objects.all()
    