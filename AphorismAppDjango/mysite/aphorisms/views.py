#### Grace Hadiyanto
#### e-mail: ifoundparis@gmail.com
#### Assignment 7
#### CS223P

from django.shortcuts import render
from aphorisms.models import Fortunes

import random
import time

# Create your views here.

random.seed() # seed random generator
fortunes = Fortunes.objects.all() # list of all fortunes

def index(request):
    today = time.strftime("%c")
    # choose a random int, randint(a, b) returns x which a <= x <= b
    # use the return value of randint to grab the fortune at the x index
    # don't use the 0 index because it's not a real aphorism
    # there are 14334 items in the database so 14333 is the last index
    x = random.randint(1, 14333)
    return render(request, 'aphorisms/index.html', { 'fortune' : fortunes[x], 
                                                     'filename' : fortunes[x].filename,
                                                     'date' : str(today) })
