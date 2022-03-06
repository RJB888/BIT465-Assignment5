from rest_framework import serializers
from .models import Dog, Breed
# import dogapi.dogs.views


class DogSerializer(serializers.HyperlinkedModelSerializer):

    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
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
                  'favorite_toy',)


class DogBreedSerializer(serializers.HyperlinkedModelSerializer):

    # dog = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='dog_detail'
    # )
    dog = DogSerializer(many=True, read_only=True)

    class Meta:
        model = Breed
        fields = (
            'url',
            'dog',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',
        )


