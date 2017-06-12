from rest_framework import serializers
from friends.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'owner_name', 'owner_friend', 'owner_suggestion')