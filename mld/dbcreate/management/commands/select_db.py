from django.core.management import BaseCommand

from dbcreate.models import AlgorithmsBook, DatasetsBook, MetricsBook


class Command(BaseCommand):

    def handle(self, *args, **options):

        select_from_algo_book = AlgorithmsBook.objects.all()
        for element in select_from_algo_book:
            print(element.id, element.algo_name)