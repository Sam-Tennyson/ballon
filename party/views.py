import io
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Category, ItemModel, Student
from .serializer import ItemSerializer, StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class StudentAPI(APIView):

    def get(self, request, id=None, format=None):
        try:
            if id is not None:
                stu = Student.objects.get(id=id)
                print(stu, "dataaa")
                serializer = StudentSerializer(stu)
                return  Response({"data": serializer.data, "msg": "This is get request"})
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return  Response({"data": serializer.data, "msg": "This is get request"})
        except:
            return  Response({"message":"Record Not Found","status": status.HTTP_404_NOT_FOUND})

    def post(self, request, format=None):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'message': "data added"}
            return Response(res, status=status.HTTP_201_CREATED)
                    
        return Response({"error": serializer.errors,"status":status.HTTP_400_BAD_REQUEST})

    def put(self, request, id, format=None):
        try:            
            stu= Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "updated"})
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message": "Record Not Exit", "status": status.HTTP_400_BAD_REQUEST})
    
    def delete(self, request, id, format=None):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"Record Deleted"})

# @csrf_exempt
# def ItemsView(request):
#     if request.method == 'GET':
#         items = ItemModel.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         json_data =  JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data) 
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ItemSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status =201)
#         return JsonResponse(serializer.errors,status = 400)

# class ListCategory(APIView):
#     def get(self, request):
#         print(request.data)
#         data = {
#             'first_name': 'grant',
#             'last_name': 'zhu'
#         }
#         return Response(data)

#     # HERE IS THE POST API
#     def post(self, request):
#         req_data = request.data
#         data = {
#             'first_name': req_data.get('first_name'),
#             'last_name': req_data.get('last_name')
#         }
#         return Response(data, status=status.HTTP_200_OK)
