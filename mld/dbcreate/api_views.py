from .serializers import AlgorithmsBookSerializer, MetricsBookSerializer
from .models import AlgorithmsBook, MetricsBook
from rest_framework import viewsets


# ViewSets define the view behavior.
class AlgorithmsBookViewSet(viewsets.ModelViewSet):
    queryset = AlgorithmsBook.objects.all()
    serializer_class = AlgorithmsBookSerializer


class MetricsBookViewSet(viewsets.ModelViewSet):
    queryset = MetricsBook.objects.all()
    serializer_class = MetricsBookSerializer
