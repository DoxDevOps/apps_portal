from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from portal.models import App
from .serializers import AppSerializer

class AppListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the app items for given requested user
        '''
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the App with given app data
        '''
        data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'url': request.data.get('url'),
            'icon':request.data.get('icon')
        }
        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)