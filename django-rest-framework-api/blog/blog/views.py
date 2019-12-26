from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pprint as pp
import json


@api_view(['GET', 'POST'])
def index(request):
    print(request)
    print(request.method)
    print(request.data)
    message = {
        "message": "This is rest framework",
        "msgno": "MSG0001"
    }

    if request.method == 'GET':
        return Response(data=message, status=status.HTTP_200_OK)
        print(request.auth)
    elif request.method == 'POST':
        pp.pprint(request.headers["Postman-Token"])
        print(request.auth)
        return Response(data=request.data, status=status.HTTP_200_OK)
