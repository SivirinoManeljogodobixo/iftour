from django.shortcuts import redirect, render
import comentario

from comentario.models import Avaliacao
from espacos.models import Sala
def novo(request, id):
    if request.POST:
        n = request.POST.get('nome')
        c = request.POST.get('comentario')
        a = int(request.POST.get('fb'))
        s = Sala.objects.get(pk = id)
        novo = Avaliacao(nome = n, comentario = c, nota = a, sala = s)
        novo.save()
        return redirect(f'/sala/{id}')
    else:
        return render(request, 'sala.html')

# Create your views here.
