from django.shortcuts import render

def welcome(request):
    return render(request, "welcome.html")

def hello(requset):
    userName = requset.GET['name']
    return render(requset,'hello.html',{'userName' : userName})

def wordCount(requset):
    return render(requset,'wordcount.html')

def wordCountAns(request):
    sentence = request.GET['sentence']
    count = len(sentence.split())
    return render(request,'wordCountAns.html',{'count' : count})