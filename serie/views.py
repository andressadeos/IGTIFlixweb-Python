from django.shortcuts import render

from . import forms
from . import models
# Create your views here.


def cadastro(request):
    print("insert")
    print(request.method)
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save(commit=True)
        else:
            print("ERROR")
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {'serie_records': serie_list, 'form': form}

    return render(request, 'serie/serie.html', data_dict)

def delete(request,id):
    print(delete)
    models.Serie.objects.filter(id=id).delete()
    form = forms.SerieForm()
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {'form': form, 'serie_records': serie_list}
    return render(request, 'serie/serie.html', data_dict)

def update(request,id):
    item = models.Serie.objects.get(id=id)
    if (request.method == "GET"):
        form = forms.SerieForm(initial={'name': item.name})
        data_dict = {'form': form}
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.descricao = form.data['name']
        item.save()
        serie_list = models.Serie.objects.order_by('name')
        data_dict = {'form': form, 'serie_records': serie_list}
        return render(request, 'serie/serie.html', data_dict)
