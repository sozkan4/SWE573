from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Annotation

def annotation_list(request):
    annotations = Annotation.objects.all()
    annotation_data = [annotation.as_dict for annotation in annotations]
    return JsonResponse(annotation_data, safe=False)

def annotation_detail(request, pk):
    annotation = get_object_or_404(Annotation, pk=pk)
    annotation_data = annotation.as_dict
    return JsonResponse(annotation_data)
