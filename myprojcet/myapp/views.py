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

    wordList = sentence.split()

    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] +=1
        else:
            wordDict[word] = 1

    return render(request,'wordCountAns.html',{'sentence' : sentence,'count' : len(wordList), 'wordDict' : wordDict.items})