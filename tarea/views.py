from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from tarea.models import Tarea

def crear(request):
    if request.method == "POST":
        tarea = Tarea.objects.create(descripcion=request.POST['descripcion'],
                                     lista_id=request.POST['lista'])
    else:
        raise Http404
    
    return HttpResponseRedirect(reverse('lista', args=[tarea.lista.codigo,]))
        