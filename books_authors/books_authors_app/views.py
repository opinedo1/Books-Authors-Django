from django.shortcuts import render, HttpResponse
# from .models import Author

# Create your views here.
def index(request):
    # context = {
    #     'authors': Author.objects.all()
    # }
    # return HttpResponse("Hello World")
    return render(request, 'index.html')
