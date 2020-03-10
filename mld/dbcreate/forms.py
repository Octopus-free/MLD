from django import forms
from django.forms import Textarea
from .models import AlgorithmsBook

class AlgoName(forms.Form):

    name = forms.CharField(label='Какой алгоритм Вас интересует?')


class AddInfoAboutAlgo(forms.ModelForm):

    class Meta:
        model = AlgorithmsBook
        fields = '__all__'
        labels = {
            'algo_name': 'Введите название алгоритма',
            'algo_desc': 'Введите описание алогритма'
        }
        widgets = {
            'algo_desc': Textarea()
            }
