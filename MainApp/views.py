from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()
    context = {'T': topics}     #key represents the variable name in the template, the value is the variable name in the view
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    t = Topic.objects.get(id=topic_id)
    entries = Entry.objects.filter(topic=t).order_by('-date_added') #the minus (-) sign means descending order
    context = {'topic':t, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')
        
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)


