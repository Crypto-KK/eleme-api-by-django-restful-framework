from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.models import Entry
from api.serializers import EntrySerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from api import custompermission

class EntryList(generics.ListCreateAPIView):
    throttle_scope = 'entries'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    name = 'entry-list'
    filter_fields = ('city','school','name')
    search_fields = ('^school',)
    ordering_fields = ('city')

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'entries'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    name = 'entry-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'entries': reverse(EntryList.name, request=request),
        })