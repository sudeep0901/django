from rest_framework.serializers import ModelSerializer
from blogapp.models import Person, LANGUAGE_CHOICES, STYLE_CHOICES


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
