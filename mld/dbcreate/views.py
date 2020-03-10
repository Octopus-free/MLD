from django.shortcuts import render, HttpResponse
from .forms import AlgoName, AddInfoAboutAlgo
from .models import AlgorithmsBook
from django.views.generic import ListView, FormView, CreateView
from django.views import View
from django.urls import reverse_lazy


class IndexFormView(FormView):

    form_class = AlgoName
    template_name = 'dbcreate/index.html'
    success_url = 'db/'

    def form_valid(self, form):
        return super().form_valid(form)


class ContactView(View):

    def get(self, request):
        return render(request, 'dbcreate/contacts.html', context={})


class AboutView(View):

    def get(self, request):
        return render(request, 'dbcreate/about.html', context={})


class DBKnowledgeListView(ListView):

    model = AlgorithmsBook
    template_name = 'dbcreate/db_knowledge.html'


class AddInfo(CreateView):

    form_class = AddInfoAboutAlgo
    model = AlgorithmsBook
    template_name = 'dbcreate/add_info.html'
    success_url = reverse_lazy('dbcreate:db_knowledge')
