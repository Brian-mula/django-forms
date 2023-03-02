from django.shortcuts import render
from home.forms import ProductForm


# Create your views here.
def homepage(request):
    if request.method == "POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProductForm()
    context={"form":form}
    return render(request,"home.html",context=context)