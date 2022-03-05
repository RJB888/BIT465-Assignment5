from rest_framework import serializers
from .models import Dog


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name',
                  'age',
                  'breed',
                  'gender',
                  'color',
                  'favorite_food',
                  'favorite_toy')
    # name = serializers.CharField(max_length=50)
    # age = serializers.IntegerField()
    # breed = serializers.CharField(max_length=100)
    # gender = serializers.CharField(max_length=100)
    # color = serializers.CharField(max_length=100)
    # favorite_food = serializers.CharField(max_length=100)
    # favorite_toy = serializers.CharField(max_length=100)
    #
    # def create(self, validated_data):
    #     return Dog.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.breed = validated_data.get('breed', instance.breed)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.favorite_food = validated_data.get('favorite_food', instance.favorite_food)
    #     instance.favorite_toy = validated_data.get('favorite_toy', instance.favorite_toy)
    #     instance.save()
    #     return instance


