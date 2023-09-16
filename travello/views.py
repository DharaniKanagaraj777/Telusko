from django.shortcuts import render
from.models import destination
# Create your views here.

def index(request):
    dest1 = destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img='destination_1.jpg'
    dest1.price = 700
    dest1.offer=True
    
    dest2 = destination()
    dest2.name = 'Hyderbad'
    dest2.desc = 'Best Briyani'
    dest2.img='destination_2.jpg'
    dest2.price = 750
    dest2.offer=False
    
    dest3 = destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'Best City'
    dest3.img='destination_3.jpg'
    dest3.price = 780
    dest3.offer=False
    
    dests = [dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})

