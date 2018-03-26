from django.shortcuts import render
from apps.web.models import Autor
# Create your views here.


def home(request):
    return render(request, 'web/home.html', locals())


def autor_detalle(request, id=None):
    print(id, "<<<")
    autor = Autor.objects.get(id=int(2))
    print(autor.get_absolute_url())
    return render(request, 'web/home.html', locals())


def autores(request):

    return render(request, "web/autores.html", locals())