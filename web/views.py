# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import *
from django.template import RequestContext

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render_to_response("index.html", {"categories": categories}, context_instance = RequestContext(request))

def products(request):
    categories = Category.objects.all()
    return render_to_response("products.html", {"categories": categories}, context_instance = RequestContext(request))

def category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    return render_to_response("category.html", {"categories": categories,"category": category}, context_instance = RequestContext(request))

def subcategory(request, category_id, subcategory_id):
    categories = Category.objects.all()
    subcategory = SubCategory.objects.get(id=subcategory_id,category_id=category_id)
    return render_to_response("subcategory.html", {"categories": categories,"subcategory": subcategory}, context_instance = RequestContext(request))

def product(request, product_id):
    categories = Category.objects.all()
    product = Product.objects.get(id=product_id)
    return render_to_response("product.html",{"categories":categories,"product":product}, context_instance = RequestContext(request))