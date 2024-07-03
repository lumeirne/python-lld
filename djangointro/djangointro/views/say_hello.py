from django.http import HttpResponse, HttpRequest

def say_hello(request):
    return HttpResponse("Welcome, Guys")

def say_hello_with_name(request, name):
    name = name.title()
    return HttpResponse(f"Hello! {name}, from Rahul(Lumeirne)")