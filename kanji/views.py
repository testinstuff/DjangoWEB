from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from kanji.models import grammarParticle, radicals
from django.views.decorators.csrf import csrf_exempt
import random
from random import randint
import time
# Create your views here.

def home(request):
    kanji_list = grammarParticle.objects.all()
    radicals_list = radicals.objects.all()
    query = request.GET.get("q")
    context = {"kanji_list":kanji_list, "radicals_list":radicals_list}
    if query:
        kanji_list = kanji_list.filter(hiragana=query)
    return render(request, "kanji/base.html", context)
@csrf_exempt
def add_kanji(request):
    kanji=request.POST["content"]
    radical = request.POST["radical"]
    if mahina == "N5":
        grammarParticle.objects.create(hiragana=kanji)
    if mahina == "Radical":
        radicals.objects.create(radical=kanji)

    return HttpResponseRedirect("/")


def delete_kanji(request, kanji_id):
    print(kanji_id)
    grammarParticle.objects.get(id=kanji_id).delete()
    return HttpResponseRedirect("/")

def kanji_info(request,kanji_id):
    context = grammarParticle.objects.get(id=kanji_id)
    return render(request, "kanji/kanji_info.html", {
    "context":context})

def radical_info(request,radical_id):
    radical_info = radicals.objects.get(id=radical_id)
    kanji_associated = grammarParticle.objects.filter(radical=radical_info.radical)
    context = {"radical_info":radical_info, "kanji_associated":kanji_associated}
    return render(request, "kanji/radical_info.html", context)

def studyn5(request):
    kanji_n5 = grammarParticle.objects.all()
    context = {"kanji_n5":kanji_n5}
    return render(request,"kanji/studyn5.html",context)

def updateDetails(request,kanji_id):
    kanji_n5 = grammarParticle.objects.all()
    details = grammarParticle.objects.filter(id=kanji_id)
    test = grammarParticle.objects.get(id=kanji_id)
    radical_associated = radicals.objects.filter(radical=test.radical)
    context = {"kanji_n5":kanji_n5, "details":details, "radical_associated":radical_associated}
    return render(request,"kanji/studyn5.html", context)

def studyRadicals(request):
    radicals_list = radicals.objects.all()
    context = {"radicals_list":radicals_list}
    return render(request,"kanji/studyradicals.html", context)

def updateRadical(request,radical_id):
    radicals_list = radicals.objects.all()
    radical_info = radicals.objects.filter(id=radical_id)
    radical_detail = radicals.objects.get(id=radical_id)
    kanji_associated = grammarParticle.objects.filter(radical=radical_detail.radical)
    context = {"radical_info":radical_info, "radicals_list":radicals_list, "kanji_associated":kanji_associated}
    return render(request, "kanji/studyradicals.html", context)



@csrf_exempt
def practiceN5(request):
    count = grammarParticle.objects.count()
    kanji_n5 = grammarParticle.objects.all()[randint(0, count - 1)]
    context = {"kanji_n5":kanji_n5}
    time.sleep(1)
    return render(request, "kanji/learningn5.html", context)


def login_page(request):
    return render(request,"kanji/login.html")

def register_page(request):
    return render(request, "kanji/register.html")
