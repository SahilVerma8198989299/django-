from django.http import HttpResponse
from django.shortcuts import render

def homepage(requests):
    data={
        'title':'home_page',
        'body':'hum hai kamaal ke.............',
        'lists':['sahil', 'harshit', 'kanika_mam'],
        'dict':[
            {'name':'sahil', 'class':'btech 3rd sem'},
            {'name':'harshit', 'class':'betach 3rd sem'}
        ],
        'pp':[1,2,3,4,5,6,7,8,9,0]
    }

    return render(requests, "index.html", data)


def hello(requests):
    return HttpResponse("hello everyone.............")
def dynamic(requests, id):
    return HttpResponse(id)
def further(requests, sahil):
    return HttpResponse(sahil)