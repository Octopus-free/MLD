from django.core.management.base import BaseCommand
from dbcreate.models import AlgorithmsBook, MetricsBook, DatasetsBook
import json

with open ('data_for_algo_book.json', 'r') as algo_from_file:
    algo_dict = json.load(algo_from_file)

with open ('data_for_metrics_book.json', 'r') as metrics_from_file:
    metrics_dict = json.load(metrics_from_file)

with open ('data_for_datasets_book.json', 'r') as datasets_from_file:
    datasets_dict = json.load(datasets_from_file)


class Command(BaseCommand):

    def handle(self, *args, **options):

        for algo_key, algo_value in algo_dict.items():
            inserting_in_algo_book = AlgorithmsBook(algo_name=algo_key, algo_desc=algo_value)
            inserting_in_algo_book.save()

        for metric_key, metric_value in metrics_dict.items():
            inserting_in_metrics_book = MetricsBook(metric_name=metric_key, metric_desc=metric_value)
            inserting_in_metrics_book.save()

        for dataset_key, dataset_value in datasets_dict.items():
            inserting_in_datasets_book = DatasetsBook(dataset_name=dataset_key, dataset_desc=dataset_value)
            inserting_in_datasets_book.save()

