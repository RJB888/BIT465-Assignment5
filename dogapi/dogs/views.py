from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dog
from .serializers import DogSerializer

# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
@api_view(['GET', 'POST'])
def dog_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        dogs_serializer = DogSerializer(dogs, many=True)
        return Response(dogs_serializer.data)
    elif request.method == 'POST':
        dogs_serializer = DogSerializer(data=request.data)
        if dogs_serializer.is_valid():
            dogs_serializer.save()
            return Response(dogs_serializer.data, status=status.HTTP_201_CREATED)
        return Response(dogs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PUT', 'POST'])
def dog_detail(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        dog_serializer = DogSerializer(dog)
        return Response(dog_serializer.data)
    elif request.method == 'PUT':
        dog_serializer = DogSerializer(dog, data=request.data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return Response(dog_serializer.data)
        return Response(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

