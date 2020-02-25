from django.http import HttpResponse           ## allows for return back information as an HTTP response
from django.shortcuts import render
import operator



def home(request):                       ## anytime someone visits the website.. it sends this request object
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #add to the dictionary
            wordDictionary[word] = 1


    sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedWords':sortedWords})
