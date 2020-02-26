from django import forms


class AlgoName(forms.Form):

    algo_name = forms.CharField(label='Какой алгоритм Вас интересует?')



