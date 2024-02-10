from django.shortcuts import render

# Create your views here.

def create(request):
    return render(request,'create.html')

def list(request):
    movie_details = {
        'movies':[
            {
            'title' : 'Godfather',
            'year' : 1990,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True,
            'img' :'actor-mukesh-image.jpg'
        },{
            'title' : 'raone',
            'year' : 1991,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : False,
            'img' :'Mukesh_malayalam.jpg'
        },{
            'title' : 'father',
            'year' : 1992,
            # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True,
            'img' :'MUKESH.jpg'

        },{
            'title' : 'God',
            'year' : 1995,
            'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : False,
            'img' :'Mukesh5.jpg'

        },{
            'title' : 'Gother',
            'year' : 1999,
            # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
            'success' : True
        }]
    }
    return render(request,'list.html',movie_details)

def edit(request):
    return render(request,'edit.html')

