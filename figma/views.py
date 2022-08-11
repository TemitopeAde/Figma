from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.views import generic
from .models import Hashes, Stories
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404


# Homepage View
def indexView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'index.html', context)


def detailView(request, slug):
    post = get_object_or_404(Stories, slug=slug)
    context = {
        "post": post
    }
    return render(request, 'detail.html', context)


def loginView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'login.html', context)


def notloggedInView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'not-logged-in.html', context)


def hashLinkView(request, slug):
    post = get_object_or_404(Stories, slug=slug)
    context = {
        "post": post
    }
    return render(request, 'link-with-hash.html', context)


def enterCodeView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'enter-code.html', context)



def addLinkView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'add-link.html', context)


def confirmView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'confirm.html', context)




def addHashView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'add-hash.html', context)


def hashAddedView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'add-hash.html', context)




def wrongCodeView(request):
    allstories = Stories.objects.filter(status=1).order_by('-created_on')
    context = {
        "post_list": allstories
    }
    return render(request, 'wrong-code.html', context)



def allHashesView(request):
    allhashes = Hashes.objects.all()
    context = {
        "allhashes": allhashes 
    }
    return render(request, 'hash.html', context)


def hashedDetailView(request, slug):
    hash = Hashes.objects.filter(title=title)
    context = {
        "hash": hash
    }
    return render(request, 'hash-feed.html', context)
