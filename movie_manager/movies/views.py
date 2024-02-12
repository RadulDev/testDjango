from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

def create(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')

        movie_obj = MovieInfo(title=title,year=year,summary=summary)
        movie_obj.save()


    return render(request,'create.html')

def list(request):
    # movie_details = {
    #     'movies':[
    #         {
    #         'title' : 'Godfather',
    #         'year' : 1990,
    #         'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
    #         'success' : True,
    #         'img' :'actor-mukesh-image.jpg'
    #     },{
    #         'title' : 'raone',
    #         'year' : 1991,
    #         'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
    #         'success' : False,
    #         'img' :'Mukesh_malayalam.jpg'
    #     },{
    #         'title' : 'father',
    #         'year' : 1992,
    #         # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
    #         'success' : True,
    #         'img' :'MUKESH.jpg'

    #     },{
    #         'title' : 'God',
    #         'year' : 1995,
    #         'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
    #         'success' : False,
    #         'img' :'Mukesh5.jpg'

    #     },{
    #         'title' : 'Gother',
    #         'year' : 1999,
    #         # 'summary' : ' Mukesh, innnocent, manya, Philomina, Thilakan',
    #         'success' : True
    #     }]
    # }
    # return render(request,'list.html',movie_details)
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    return render(request,'list.html', {'movies':movie_data})

def edit(request):
    return render(request,'edit.html')

