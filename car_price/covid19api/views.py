from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            globalSummary = json['Global']
            countries = json['Countries'][76] 
            data = False
        except:
            data = True    
    return render(request,'index.html',{'globalSummary':globalSummary,'countries':countries})


def allcountry(request):
    data = True
    result2 =None
    allcountries = None    
    while(data):
        try:
            result2 = requests.get('https://api.covid19api.com/summary')
            json = result2.json()
            allcountries = json['Countries']
            data = False
        except:
            data = True    
    return render(request,'country.html',{'allcountries':allcountries})

