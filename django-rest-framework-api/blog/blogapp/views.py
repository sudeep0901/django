# from django.shortcuts import render

from rest_framework.views import APIView
from blogapp.models import Person
from blogapp.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PersonView(APIView):

    def get_object(self):
        try:

            return Person.objects.all()
        except Person.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, format=None):
        # queryset = Person.objects.all()
        queryset = self.get_object()
        serializer = PersonSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = PersonSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        try:
            if serializer.is_valid():
                print("checking vailidity. . . . . . .")
                print(serializer.validated_data)
                serializer.save()
                return Response(daserializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # pass
            #     print(e)
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
