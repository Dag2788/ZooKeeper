# Create your views here.
#added by Jesus June 11 2015
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context,loader
from ZooKeeper.store.models import Pets, Products


def index (request):
    return render_to_response('index.html')

def contact (request):
    return render_to_response('contact.html')
def pets_and_products(request):
    pet_results = []
    pet_results = Pets.objects.all()
    for p in pet_results:
        p.picture = str(p.picture).replace('ZooKeeper','')
    context = Context({
		'pets': pet_results
	})
    template = loader.get_template('pets_and_products.html')
    return HttpResponse(template.render(context))
    # return render_to_response('pets_and_products.html')

def pets(request):
    pet_results = []
    pet_results = Pets.objects.all()
    for p in pet_results:
        p.picture = str(p.picture).replace('ZooKeeper','')
    context = Context({
		'pets': pet_results
	})
    template = loader.get_template('pets_and_products.html')
    return HttpResponse(template.render(context))

def products(request):
    # pet_results = []
    product_results = []
    # pet_results = Pets.objects.all()
    product_results = Products.objects.all()
    # context = {"pets": pet_results, "products": product_results}
    context = Context({
		'products': product_results
	})
    template = loader.get_template('products.html')
    return HttpResponse(template.render(context))

def blog(request):
    return render_to_response('blog.html')

def bc(request):
    return render_to_response('bc_index.html')
