from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import employee,stud, cust
from .serializers import employeeSerializer, studSerializer, studSerializer1, UserSerializer, custSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import permissions
from emploapp.permissions import IsOwnerOrReadOnly

# Hyperlink
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users': reverse('user-list', request=request, format=format),
        'Students': reverse('stude-list', request=request, format=format),
        'Employees': reverse('emplo-list', request=request, format=format)
    })

# User and Permission
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Studentlist(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = studSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GenericstudListCreate(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = studSerializer

class Emplolist(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Studentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stud.objects.all()
    serializer_class = studSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class Emplodetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class Emplist(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        employee1 = employee.objects.all()
        serializer = employeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        # print(data)
        serializer = employeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        else:
            return Response("faill")

class Empdetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk=None):
        employee1 = employee.objects.get(id=pk)
        serializer = employeeSerializer(employee1, many=False)
        return Response(serializer.data)

class Empupdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = employeeSerializer
    def put(self, request,pk=None):
        employee1 = employee.objects.get(id=pk)
        print(employee1)
        serializer = employeeSerializer(employee1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        else:
            return Response("faill")

class Empdelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk=None):
        employee1 = employee.objects.get(id=pk)
        employee1.delete()
        return Response("Success")

# Generic View
class GenericempListCreate(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class GenericempRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


# Mixins
class EmplistMixins(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class EmpdetailedMixins(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):



    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Viewsets

# class EmploViewsets(viewsets.ViewSet):
#     def list(self, request):
#         queryset = employee.objects.all()
#         serializer = employeeSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = employee.objects.all()
#         if pk is not None:
#             employee1 = get_object_or_404(queryset, pk=None)
#             serializer = employeeSerializer(employee1)
#             return Response(serializer.data)

class StudViewset(viewsets.ModelViewSet):
    queryset = stud.objects.all()
    serializer_class = studSerializer

    @action(detail=False, methods=['get'])
    def cool_stud(self, request):
        stude = stud.objects.filter(pk=3)
        serializer = studSerializer(stude, many=True)
        return Response({'data': serializer.data})



# Fucntion based view
@api_view(['GET'])
def Studlist(request):
    stud1 = stud.objects.all()
    serializer = studSerializer1(stud1, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Studdetail(request, pk):
    stud1 = stud.objects.get(id=pk)
    serializer = studSerializer1(stud1, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Studcreate(request):
    data = request.data
    serializer = studSerializer1(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Success")
    else :
        return Response("Faill")

@api_view(['PUT'])
def Studupdate(request, pk):
    stud1 = stud.objects.get(id=pk)
    serializer = studSerializer1(stud1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Success")
    else:
        return Response("Faill")

@api_view(['DELETE'])
def Studdelete(request, pk=None):
    stud1 = stud.objects.get(id=pk)
    stud1.delete()
    return Response("Success")


# for testing

class Custlist(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        cust1 = cust.objects.all()
        serializer = custSerializer(cust1, many=True)
        return Response(serializer.data)


class Custdetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        cust1 = cust.objects.get(id=pk)
        serializer = custSerializer(cust1, many=False)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        # print(data)
        serializer = custSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        else:
            return Response("faill")



class Custupdate(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = custSerializer
    def put(self, request,pk=None):
        cust1 = cust.objects.get(id=pk)
        print(cust1)
        serializer = custSerializer(cust1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        else:
            return Response("faill")

class Custdelete(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk=None):
        cust1 = cust.objects.get(id=pk)
        cust.delete()
        return Response("Success")
