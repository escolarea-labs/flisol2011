from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from tarea.models import Tarea
from django.utils import simplejson

def crear(request):
    if request.method == "POST":
        tarea = Tarea.objects.create(descripcion=request.POST['descripcion'],
                                     lista_id=request.POST['lista'])
    else:
        raise Http404

    if request.is_ajax():
        result = {"id":tarea.id}
        return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        return HttpResponseRedirect(reverse('lista', args=[tarea.lista.codigo,]))
        