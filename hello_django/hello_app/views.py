from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def print_hello(request):
    # return HttpResponse("<b>hello django</b>")
    movie_details = {
        'movies':[
            {
            'title' : 'Godfather',
            'year' : 1990,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True
        },{
            'title' : 'raone',
            'year' : 1991,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : False
        },{
            'title' : 'father',
            'year' : 1992,
            # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True
        },{
            'title' : 'God',
            'year' : 1995,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : False
        },{
            'title' : 'Gother',
            'year' : 1999,
            # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True
        }]
    }

    return render(request,'hello.html',movie_details)