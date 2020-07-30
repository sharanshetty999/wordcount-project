from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase count
            worddictionary[word] += 1
        else:
            #add word
            worddictionary[word] = 1
    sortedlist = sorted(worddictionary.items(),key= operator.itemgetter(1), reverse= True)
    return render(request, 'count.html', {'text': text,'wordcount': len(wordlist), 'worddictionary': sortedlist})

def about(request):
    return render(request, 'about.html')
