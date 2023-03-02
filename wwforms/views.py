from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse("404: This page does not exist")

def handler501(request,*args, **argv):
    return HttpResponse("500: The server encountered an error")