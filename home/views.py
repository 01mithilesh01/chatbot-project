from django.shortcuts import render

# Create your views here.
def first_page(request) :
    return render(request, 'home/first_page.html')

def feedback(request) :
    return render(request, 'home/feedback.html')

def contactus(request) :
    return render(request, 'home/contactus.html')

def info(request) :
    return render(request, 'home/info.html')

def chat(request) :
    name = request.GET['name']
    return render(request, 'home/chat.html', {'name' : name})
