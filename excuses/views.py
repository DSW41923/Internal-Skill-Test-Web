from django.shortcuts import render
from excuses.models import Excuse
import random
# Create your views here.

def excuses(request):
	excuses_list = Excuse.objects.all()
	if len(excuses_list) == 0:
		return render(request, 'index.html', {'current_excuse': "Nothing in DB!!!"})
	else:
		e = excuses_list[random.randint(0, len(excuses_list)-1)]
		return render(request, 'index.html', {'current_excuse': e.content})