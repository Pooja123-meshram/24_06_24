from django.http import  HttpResponse

def feature1(request):
    return  HttpResponse('<h1> this is feature 1</h1>')
