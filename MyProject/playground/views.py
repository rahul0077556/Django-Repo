from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return render(request,'index.html',{'name':'Virat',
                                        'salary':'10000'})


