from django.shortcuts import render
from .models import Gallery, Text
# Create your views here.

def home(request):
    context = {}
    context['gallery1'] = Gallery.objects.get(id=1)
    context['gallery2'] = Gallery.objects.get(id=2)
    context['gallery3'] = Gallery.objects.get(id=3)
    context['gallery4'] = Gallery.objects.get(id=4)
    context['gallery5'] = Gallery.objects.get(id=5)
    context['gallery6'] = Gallery.objects.get(id=6)
    context['gallery7'] = Gallery.objects.get(id=7)
    context['gallery8'] = Gallery.objects.get(id=8)
    context['gallery9'] = Gallery.objects.get(id=9)
    context['gallery10'] = Gallery.objects.get(id=10)
    context['gallery11'] = Gallery.objects.get(id=11)
    context['text1'] = Text.objects.get(id=1)
    context['text2'] = Text.objects.get(id=2)
    context['text3'] = Text.objects.get(id=3)
    context['text4'] = Text.objects.get(id=4)
    context['text5'] = Text.objects.get(id=5)
    context['text6'] = Text.objects.get(id=6)
    context['text7'] = Text.objects.get(id=7)
    context['text8'] = Text.objects.get(id=8)
    context['text9'] = Text.objects.get(id=9)


    return render(request,'onepage.html',context)
"""
def about(request):
    context = {}
    context['gallerys'] = Gallery.objects.get(author='LHN')
    context['texts'] = Text.objects.get(author='LHN')
    return render(request,'about.html',context)

def typography(request):
    context = {}
    context['gallerys'] = Gallery.objects.get(author='LHN')
    context['texts'] = Text.objects.filter(author='LHN')
    return render(request,'typography.html',context)

def gallery(request):
    context = {}
    context['gallerys'] = Gallery.objects.get(author='LHN')
    context['texts'] = Text.objects.get(author='LHN')
    return render(request,'gallery.html',context)

def contact(request):
    context = {}
    context['gallerys'] = Gallery.objects.get(author='LHN')
    context['texts'] = Text.objects.get(author='LHN')
    return render(request,'contact.html',context)
"""