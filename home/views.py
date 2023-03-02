from django.shortcuts import render
from .forms import ProductForm


# Create your views here.
def homepage(request):
    form=ProductForm()
    context={"form":form}
    return render(request,"home.html",context=context)