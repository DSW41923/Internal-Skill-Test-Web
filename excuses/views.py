from django.shortcuts import render
from excuses.models import Excuse
import random
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.
class ExcuseForm(forms.ModelForm):
    class Meta:
        model = Excuse
        fields = ['provider', 'content', ]

def show_excuses(request):
    excuses_list = Excuse.objects.all()
    if len(excuses_list) == 0:
        return render(request, 'index.html', {'current_excuse': "Nothing in DB!!!"})
    else:
        e = excuses_list[random.randint(0, len(excuses_list)-1)]
        return render(request, 'index.html', {'current_excuse': e.content, 'current_excuse_provider':e.provider})

def adding_excuses(request):
    if request.method == 'POST':
        form = ExcuseForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/')

    form = ExcuseForm()
    return render(request, 'add.html', {'form': form})