from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


# Create your views here.

def index(request):

    # if logined, show home.
    # else, redirect to login.

    id = request.session['token']


def login(request):
    if request.method != "POST":
        return Http404("Request destination does not exist")

    id = request.POST['id']
    pw = request.POST['password']



def logout(request):
    request.session.clear()
    return redirect('/')

def get_post(request):

def save_post(request):

def delete_post(request):

def update_post(request):
