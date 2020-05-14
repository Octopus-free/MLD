from .serializers import AlgorithmsBookSerializer, MetricsBookSerializer
from .models import AlgorithmsBook, MetricsBook
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# ViewSets define the view behavior.
class AlgorithmsBookViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser|ReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = AlgorithmsBook.objects.all()
    serializer_class = AlgorithmsBookSerializer


class MetricsBookViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    queryset = MetricsBook.objects.all()
    serializer_class = MetricsBookSerializer
