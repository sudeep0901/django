# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views.decorators.csrf import csrf_exempt
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser

# Create your views here.

"""function based views
# ------------------------------------"""
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status=201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         # return JsonResponse(serializer.errors, statuss=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """

#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # return HttpResponse(status=404)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         # serializer = SnippetSerializer(snippet, data=data)
#         serializer = SnippetSerializer(snippet, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)
#             return Response(serializer.data)

#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         # return HttpResponse(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)


""" Class based view """


# class SnippetList(APIView):
#     """
#     list all snippets
#     """
#     @csrf_exempt
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     @csrf_exempt
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)

#         except Snippet.Does_Not_Exist:
#             raise Http404
#     @csrf_exempt
#     def get(self, request, pk):
#         # snippet = Snippet.objects.get(pk=pk)
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     @csrf_exempt
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     @csrf_exempt
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
                    
#         queryset = Snippet.objects.all()
#         serializer_class = SnippetSerializer

#         def get(self, request, *args, **kwargs):
#             return self.retrieve(request, *args, **kwargs)

#         def put(self, request, *args, **kwargs):
#             return self.update(request, *args, **kwargs)

#         def delete(self, request, *args, **kwargs):
#             return self.destroy(request, *args, **kwargs)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer