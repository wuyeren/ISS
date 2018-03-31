from django.http import HttpResponse
from score_picture import function
from django.shortcuts import render
import os
from ISS import settings

def index(request):
    return render(request, 'input.html')

def score(request):

    if request.method == "POST":
        f1 = request.FILES['image']
        name = request.POST['name']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)
    score = {}
    tester_answer = function.read_image(fname)
    score['score'] = function.score(tester_answer, function.key)
    score['name'] = name
    return render(request, 'score.html', score)
