from django.shortcuts import render

# Create your views here.
def service(request):
    return render (request, 'pages/service.html')
def doctor(request):
    return render (request, 'pages/doctor.html')
def book(request):
    return render (request, 'pages/book.html')
def contact(request):
    return render (request, 'pages/contact.html')