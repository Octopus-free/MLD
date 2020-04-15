from django.shortcuts import render, HttpResponse
from .forms import AlgoName, AddInfoAboutAlgo
from .models import AlgorithmsBook
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator


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

    # model = AlgorithmsBook
    queryset = AlgorithmsBook.objects.select_related()
    template_name = 'dbcreate/db_knowledge.html'
    paginate_by = 1


class AddInfo(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    login_url = ('ManagingUsers:login')
    form_class = AddInfoAboutAlgo
    model = AlgorithmsBook
    template_name = 'dbcreate/add_info.html'
    success_url = reverse_lazy('dbcreate:db_knowledge')
    raise_exception = True
    permission_denied_message = ' Зайдите с правами суперпользователя'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        permission_denied_message = 'Зайдите с правами суперпользователя'
        return self.request.user.is_superuser

    def get_permission_denied_message(self):
        return self.permission_denied_message


