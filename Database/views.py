from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from Database.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status 
from .models import Database
from .serializers import DatabaseSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class Database_Get_Update_Delete_Api(RetrieveUpdateDestroyAPIView):
    serializer_class = DatabaseSerializer

    def get_queryset(self, pk):
        try:
            data = Database.objects.get(pk=pk)
        except Database.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return data

    # Get Data
    def get(self, request, pk):

        query = self.get_queryset(pk)
        serializer = DatabaseSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update Data
    def put(self, request, pk):
        
        query = self.get_queryset(pk)
        serializer = DatabaseSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Data
    def delete(self, request, pk):

        query = self.get_queryset(pk)
        query.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
   

class Database_Get_Post_Api(ListCreateAPIView):
    serializer_class = DatabaseSerializer
  
    def get_queryset(self):
       queryset = Database.objects.all()
       return queryset

    # Get Data
    def get(self, request):
        queryset = self.get_queryset()
        paginate_queryset = self.paginate_queryset(queryset)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create Data
    def post(self, request):
        serializer = DatabaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
