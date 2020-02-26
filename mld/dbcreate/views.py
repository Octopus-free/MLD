from django.shortcuts import render, HttpResponse
from .forms import AlgoName
from .models import AlgorithmsBook


def index(request):
    form = AlgoName()
    return render(request, 'dbcreate/index.html', context={'form': form})


def contacts(request):
    return render(request, 'dbcreate/contacts.html', context={})


def about(request):

    return render(request, 'dbcreate/about.html', context={})


def db_knowledge(request):

    select_from_db_algo_book = AlgorithmsBook.objects.all()
    return render(request, 'dbcreate/db_knowledge.html', context={'algo_book': select_from_db_algo_book})
