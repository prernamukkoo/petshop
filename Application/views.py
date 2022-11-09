from django.shortcuts import render

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
    return render(request, template, context)

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

