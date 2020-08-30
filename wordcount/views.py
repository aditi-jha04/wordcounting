from django.http import HttpResponse   
from django.shortcuts import render  
import operator 

def home(request):
    return render(request, 'home.html')   

def count(request):
    fulltext = request.GET['fulltext']
    wordlist =fulltext.split()

    worddictionary

    for word in wordlist:   
        if word in worddictionary:
            #increase
            
        
                #add to dictionary
                worddictionary[word] = 1

                sorted(worddictionary.items(), key=operator.itemgetter(1))

    return render(request, 'count.html', {'filltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary.items()})