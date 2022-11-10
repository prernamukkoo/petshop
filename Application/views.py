from django.shortcuts import render
# from .models import Info
from .form import InfoForm
# Create your views here.

def index(request):
    template = 'Application/index.html'
    context = {}
    return render(request, template, context)

def about(request):
    template = 'Application/about.html'
    context = {}
    return render(request, template, context)

def blog(request):
    template = 'Application/blog.html'
    context = {}
    return render(request, template, context)

def contact(request):
    template = 'Application/contact.html'
    context = {}
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("save")
        else:
            print(form.errors)
    return render(request, template, context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def saveInfoDAta(request):
    form = InfoForm(request.POST)
    if form.is_valid():
        form.save()
        context = {
            'status': 202
        }
    else:
        context = {
            'status': 400
        }
    return JsonResponse(context)

def detail(request):
    template = 'Application/detail.html'
    context = {}
    return render(request, template, context)

def price(request):
    template = 'Application/price.html'
    context = {}
    return render(request, template, context)

def product(request):
    template = 'Application/product.html'
    context = {}
    return render(request, template, context)

def service(request):
    template = 'Application/service.html'
    context = {}
    return render(request, template, context)

def team(request):
    template = 'Application/team.html'
    context = {}
    return render(request, template, context)

def testimonial(request):
    template = 'Application/testimonial.html'
    context = {}
    return render(request, template, context)

