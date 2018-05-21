# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
   # return HttpResponse("Welcome to my blog index")
# Create your views here.
    return render(request,'blog2/index2.html',context={'title':'my blog first page','welcome':'welcome to my blog'})


