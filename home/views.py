from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print 'index'
    # return HttpResponse('test')
    context = {
        'title': 'Welcome to My First Django App',
        'contents': [
            'We love Sushi.',
            'Sushi eats human',
            'Dead Sushi',
        ],
    }
    return render(request, 'home/index.html', context)

