from .models import Employee
from .Serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
from rest_framework import generics
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination

class PostLimit(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
class PostPage(PageNumberPagination):
    page_size = 5


class PostEmpList(ListAPIView):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    pagination_class = PostPage

class EmpListView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    serializer_class = EmpSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]



    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request,id=None):
        return self.create(request,id)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)













