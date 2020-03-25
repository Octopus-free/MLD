from django.db import models
from ManagingUsers.models import MLDUser


# класс для создания таблицы AlgorithmsBook
# справочник аглоритмов машинного обучения
class AlgorithmsBook(models.Model):

    user = models.ForeignKey(MLDUser, on_delete=models.CASCADE)

    # поле для хранения имени алгоритма
    algo_name = models.CharField(max_length=50, unique=True)

    # поля для хранения краткого описания алгоритма
    algo_desc = models.CharField(max_length=512)

    # функция для отображения поля algo_name
    # в admin консоли
    def __str__(self):
        return self.algo_name


# класс для создания таблицы MetricsBook
# справочник метрик машинного обучения
class MetricsBook(models.Model):

    # поле для хранения имени метрики алгоритма
    metric_name = models.CharField(max_length=50, unique=True)

    # поля для хранения краткого описания метрики алгоритма
    metric_desc = models.CharField(max_length=512)

    # функция для отображения поля metric_name
    # в admin консоли
    def __str__(self):
        return self.metric_name


# класс для создания таблицы Datasets
# справочник датасетов
class DatasetsBook(models.Model):

    # поля для хранения имени датасета
    dataset_name = models.CharField(max_length=50, unique=True)

    # поля для хранения краткого описания датасета
    dataset_desc = models.CharField(max_length=512)

    # функция для отображения поля dataset_name
    # в admin консоли
    def __str__(self):
        return self.dataset_name


