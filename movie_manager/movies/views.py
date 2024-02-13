from django.shortcuts import render
from . models import MovieInfo

from . forms import MovieForm
# Create your views here.

def create(request):
    frm= MovieForm()
    if request.POST:
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # summary = request.POST.get('summary')
        # movie_obj = MovieInfo(title=title,year=year,summary=summary)
        # movie_obj.save()

        frm = MovieForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
        else:
            frm=MovieForm()


    return render(request,'create.html',{'frm': frm})

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

def edit(request,pk):

    edit_instance = MovieInfo.objects.get(pk=pk)
    if request.POST:
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # summary = request.POST.get('summary')
        # edit_instance.title=title
        # edit_instance.year=year
        # edit_instance.summary=summary
        # edit_instance.save()
        frm=MovieForm(request.POST,instance=edit_instance)
        if frm.is_valid():
            edit_instance.save()
    else:
        frm = MovieForm(instance=edit_instance)

    return render(request,'create.html',{'frm': frm})
    # return render(request,'edit.html')


def delete(request,pk):
    del_instance = MovieInfo.objects.get(pk=pk)
    del_instance.delete()

    movie_data = MovieInfo.objects.all()
    print(movie_data)
    return render(request,'list.html', {'movies':movie_data})