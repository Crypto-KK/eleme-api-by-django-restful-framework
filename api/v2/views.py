from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api import views

class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'items': reverse(views.EntryList.name, request=request),
        })