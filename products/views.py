from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")


def product_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 #render html page
    return HttpResponse(f"Product id {obj.pk}")


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}, status=404) #return JSON
    return JsonResponse({"id": obj.pk})

# class HomeView():
#     pass
