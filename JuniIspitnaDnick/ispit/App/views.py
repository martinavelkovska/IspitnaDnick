from django.shortcuts import render, redirect

from . models import Product,Kategorija
from .forms import ProductForm
# Create your views here.


def index(request):

    qs = Kategorija.objects.all()

    #context = {"products": qs,}
    return render(request, "index.html", {"kategorii": qs})

def outofstock(request):
    if request.method == "POST":
        form_data = ProductForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            product = form_data.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("outofstock")

    qs = Product.objects.filter(kolicina=0, kategorija=True).all()

    return render(request, "products.html", {"outofstock": qs, "form": ProductForm, })
