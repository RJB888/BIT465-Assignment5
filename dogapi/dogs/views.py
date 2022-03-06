
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Dog, Breed
from .serializers import DogSerializer, DogBreedSerializer


class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogBreedSerializer
    name = 'breed_list'


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogBreedSerializer
    name = 'breed_detail'


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog_list'


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog_detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api_root'

    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogList.name, request=request),
            'breeds': reverse(BreedList.name, request=request)
        })

