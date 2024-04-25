from django.http import Http404
from django.shortcuts import render
from todo_app.models import TodoModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import TodoListSerializer, TodoAddSerializer, TodoPutSerializer
from rest_framework.permissions import AllowAny
from utils.get_ip import get_user_ip
from django.contrib.auth.models import User



class TodoListApi(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TodoListSerializer

    def get_queryset(self):
        ip = get_user_ip(self.request)
        user, create = User.objects.get_or_create(username=ip)

        todos = TodoModel.objects.filter(owner=user)
        return todos


class AddTodoApi(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TodoAddSerializer
    
    def perform_create(self, serializer):
        if serializer.is_valid():
                
            ip = get_user_ip(self.request)
            user, create = User.objects.get_or_create(username=ip)
            title = serializer.data.get('title')
    
            c_todo = TodoModel.objects.create(owner=user, title=title)
            
            return Response({'status':'created'}, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

class UpdateDeleteTodoApi(APIView):
    
    def get_todo(self, slug):
    
        ip = get_user_ip(self.request)
        user, create = User.objects.get_or_create(username=ip)        

        todo = TodoModel.objects.filter(owner=user, slug=slug).first()
        if todo is not None:
            return todo
        raise Http404

    def get(self, request, slug):
        todo = self.get_todo(slug)
        serializer = TodoListSerializer(todo)

        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, slug):
        todo = self.get_todo(slug)
        seralizer = TodoPutSerializer(todo, data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status.HTTP_200_OK)

        return Response(seralizer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        todo = self.get_todo(slug).delete()
        return Response({'status':'ok'}, status.HTTP_200_OK)