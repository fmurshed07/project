from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>This is Homepage<h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")
#
# def contact(request):
#     return HttpResponse("<h1>This is contact page<h1> <a href='/'>Homepage</a> <a href='/about/'>About</a>")
#
# def about(request):
#     return HttpResponse("<h1>About us<h1> <a href='/'>Homepage</a> <a href='/contact/'>Contact </a>")

# def index(request):
#     return HttpResponse("<h1>I'm from first app</h1>")
#
# def contact(request):
#     return HttpResponse("<h1>I'm contact page</h1>")

def index(request):
    diction = {'text_1':'I am learning django'}
    return render(request, 'first_app/index.html', context=diction)
