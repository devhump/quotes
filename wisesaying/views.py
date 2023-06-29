from django.shortcuts import render
from wisesaying.models import Wisesaying
import random

max_len = len(Wisesaying.objects.all())

# Create your views here.
def index(request):
    random_num = random.randint(1, max_len)
    wise = Wisesaying.objects.get(id=random_num)
    
    context = {
        "wise" : wise,
    }
    return render(request, 'wisesaying/index.html', context)