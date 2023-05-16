from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from app.yuyakake.models import CakeMeringue, CakeBase, CakeLayer, CakeSize, CakeSample
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from app.yuyakake.models import CakeMeringue
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageOps

class CreateOrder(LoginRequiredMixin, CreateView):
    template_name = 'orders/new_order.html'

@login_required
def cargar_merengue(request):
    objs = CakeMeringue.objects.filter(disponible=True)
    data = [{'id': obj.id, 'name': obj.name} for obj in objs]
    return JsonResponse(data, safe=False)


@login_required
def cargar_base(request):
    objs = CakeBase.objects.filter(disponible=True)
    data = [{'id': obj.id, 'name': obj.name} for obj in objs]
    return JsonResponse(data, safe=False)


@login_required
def cargar_pisos(request):
    objs = CakeLayer.objects.filter(disponible=True)
    data = [{'id': obj.id, 'name': obj.name} for obj in objs]
    return JsonResponse(data, safe=False)

@login_required
def cargar_size(request):
    objs = CakeSize.objects.filter(disponible=True)
    data = [{'id': obj.id, 'name': obj.name} for obj in objs]
    return JsonResponse(data, safe=False)

from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET'])
def get_merengue(request):
    merengue_id = request.GET.get('id')
    print(merengue_id)
    merengue = get_object_or_404(CakeMeringue, id=merengue_id)
    return JsonResponse({'merengue': merengue.serialize()})


@login_required
@require_http_methods(['GET'])
def get_base(request):
    base_id = request.GET.get('id')
    base = get_object_or_404(CakeBase, id=base_id)
    return JsonResponse({'base': base.serialize()})


@login_required
@require_http_methods(['GET'])
def get_pisos(request):
    pisos_id = request.GET.get('id')
    pisos = get_object_or_404(CakeLayer, id=pisos_id)
    return JsonResponse({'pisos': pisos.serialize()})


@login_required
@require_http_methods(['GET'])
def get_size(request):
    size_id = request.GET.get('id')
    size = get_object_or_404(CakeSize, id=size_id)
    return JsonResponse({'size': size.serialize()})



@require_http_methods(['GET'])
def get_cakesamples(request):
    cakesamples = CakeSample.objects.all().order_by('cake__rating')
    data = []
    if cakesamples:
        for cakesample in cakesamples:
            # image_temp = Image.open(cakesample.image.url)
            # image_temp = ImageOps.fit(image_temp, (800, 600), Image.ANTIALIAS)
            # image_temp.save(cakesample.image.url)
            data.append({
                'id': cakesample.id,
                'name': cakesample.name,
                'description': cakesample.description,
                'image_url': cakesample.image.url
            })
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(
            {'error': 'No se encontró ninguna muestra de pastel que coincida con los valores dados.'})


def get_cake_sample(base, merengue, size, layers):
    """
    Función para buscar objetos CakeSample que coincidan con los objetos CakeBase, CakeMeringue, CakeSize y CakeLayer dados.
    Si se encuentran objetos CakeSample que coincidan, se devuelve una lista con todos los objetos encontrados. Si no se encuentra ningún objeto CakeSample que coincida, se devuelve None.
    """
    cake_samples = CakeSample.objects.filter(base=base, meringue=merengue, size=size, layers=layers)
    if cake_samples.exists():
        return list(cake_samples)
    else:
        return None



@login_required
@csrf_exempt
def get_cake_sample_ajax(request):
    """
    Vista para obtener un objeto CakeSample buscándolo por los atributos base, merengue, size y layers mediante una llamada Ajax con el método POST.
    Los valores de los atributos se pasan en el cuerpo de la solicitud como datos POST.
    """
    if request.method == 'POST':
        base_id = request.POST.get('base_id')
        merengue_id = request.POST.get('merengue_id')
        size_id = request.POST.get('size_id')
        layers_id = request.POST.get('layers_id')

        # Se obtienen los objetos CakeBase, CakeMeringue, CakeSize y CakeLayer correspondientes a los IDs dados
        base = CakeBase.objects.get(id=base_id)
        merengue = CakeMeringue.objects.get(id=merengue_id)
        size = CakeSize.objects.get(id=size_id)
        layers = CakeLayer.objects.get(id=layers_id)

        # Se busca el objeto CakeSample que coincida con los valores dados
        cake_samples = get_cake_sample(base, merengue, size, layers)

        if cake_samples is not None:
            # Se convierte cada objeto CakeSample a un diccionario de Python serializable
            response_data = []
            for cake_sample in cake_samples:
                cake_sample_dict = {
                    'name': cake_sample.name,
                    'description': cake_sample.description,
                    'image_url': cake_sample.image.url,
                    'filling': cake_sample.filling
                }
                response_data.append(cake_sample_dict)

            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse(
                {'error': 'No se encontró ninguna muestra de pastel que coincida con los valores dados.'})
