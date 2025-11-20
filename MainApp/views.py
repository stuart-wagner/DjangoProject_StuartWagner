from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()
    context = {'T': topics}     #key represents the variable name in the template, the value is the variable name in the view
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    
