from django.core.management import BaseCommand

from dbcreate.models import AlgorithmsBook, DatasetsBook, MetricsBook


class Command(BaseCommand):

    def handle(self, *args, **options):

        algo_name_list = []

        select_from_algo_book = AlgorithmsBook.objects.all()
        for element in select_from_algo_book:
            algo_name_list.append(element.algo_name)

        print(algo_name_list)


