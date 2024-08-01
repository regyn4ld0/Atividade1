from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.utils.timezone import now
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView


#def home(request):
 #   return render(request,"hello2/home.html")

class HomeListView(ListView):
    model = LogMessage
    template_name = 'hello2/home.html' #Especificando o nome do template (se necessário)
    context_object_name = 'message_list'

def get_context_data(self, **kwargs):
    context = super(HomeListView, self).get_context_data(**kwargs)
    return context


def hello_there(request, name):
    return render(
        request,
        'hello_there.html',
        {
            'name' : name,
            'date' : datetime.now()
        }
    )

def about(request):
    return render(request,"hello2/about.html")

def contact(request):
    return render(request,"hello2/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = now()
            message.save()
            return redirect("home")
    
     # Se não for POST ou se o formulário não for válido, renderize o formulário  
    return render(request, "hello2/log_message.html", {"form": form})