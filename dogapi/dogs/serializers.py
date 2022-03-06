from rest_framework import serializers
from .models import Dog
from .models import Breed


class DogBreedSerializer(serializers.HyperlinkedModelSerializer):
    # this links the 'dogs' related_name with the models related_name in the foreign key
    dogs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='dog-detail'
    )

    class Meta:
        model = Breed
        fields = (
            'url',
            'dogs',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds'
        )


class DogSerializer(serializers.HyperlinkedModelSerializer):

    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')  #THis should display the dog breed instead of the breed id
    gender = serializers.ChoiceField(choices=Dog.GENDER_OPTIONS)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta:
        model = Dog
        fields = ('url',
                  'name',
                  'age',
                  'breed',
                  'gender',
                  'gender_description',
                  'color',
                  'favorite_food',
                  'favorite_toy')



