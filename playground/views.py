from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, World")

def say_hello_html(request):
    return render(request, "playground/hello.html", {'name':'3반!!!', 'greeting' : '반갑다'})

def say_bye(request):
    context = {
        'name' : '박선주',
        'bye' : '안녕히계세요',
    }
    return render(request, "playground/bye.html", context=context)
