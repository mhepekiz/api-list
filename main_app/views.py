from django.shortcuts import render
import requests

# Create your views here.
# def home(request):
#     return render(request, 'main_app/home.html', {'todos': 'These will be the todos'})



def home(request):
   # get the list of todos
   response = requests.get('https://api.publicapis.org/entries')
   # transfor the response to json objects
   todos = response.json()
   return render(request, "main_app/zome.html", {"todos": todos})

