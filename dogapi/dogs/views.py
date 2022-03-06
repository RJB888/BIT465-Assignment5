
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Dog
from .models import Breed
from .serializers import DogSerializer
from .serializers import DogBreedSerializer


class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogBreedSerializer
    name = 'breedList'


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = DogBreedSerializer
    name = 'breedDetail'


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dogList'


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dogDetail'


class ApiRoot(generics.GenericAPIView):
    name = 'api_root'

    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogList.name, request=request),
            'breeds': reverse(BreedList.name, request=request)
        })

