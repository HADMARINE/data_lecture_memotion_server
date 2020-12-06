import datetime

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from data_lecture_memotion_server.settings import SECRET_KEY
from memotion.models import Memo, User


def index_page(request):
    user_id = request.session.get("user_id", None)

    if user_id is None:
        # Redirect to login
        return HttpResponseRedirect("/login")

    memo_list = Memo.objects.get(user_id=user_id).order_by('-pub_date')
    context = {'memo_list': memo_list}
    return render(request, 'memotion/index_page.html', context)


def get_memo(request, memo_id):
    user_id = request.session.get('user_id', None)
    if user_id is None:
        return HttpResponseRedirect('/login')

    selected_memo = Memo.objects.get(user_id=user_id)
    return render(request, 'memotion/memo.html', {'selected_memo': selected_memo})


def save_memo(request, memo_id):
    selected_memo = get_object_or_404(Memo, pk=memo_id)
    title = request.POST.get('title', 'wow')
    if title == '':
        title = '제목 없음'

    content = request.POST.get('content', 'hello')
    private = request.POST.get('isChecked', False)
    selected_memo.title = title
    selected_memo.content = content
    selected_memo.private = private
    selected_memo.save()
    return HttpResponseRedirect(reverse('memotion:index_page', args=()))


def create_memo(request):
    memo = Memo()
    memo.title = ""
    memo.content = ""
    memo.pub_date = datetime.datetime.now()
    memo.save()

    return render(request, 'memotion/memo.html', {'selected_memo': memo})


def delete_memo(request, memo_id):
    Memo.objects.filter(pk=memo_id).delete()
    return HttpResponseRedirect(reverse('memotion:index_page', args=()))


def create_secret(pw):
    enc_pw = SECRET_KEY.encrypt(
        pw,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return enc_pw


def login(request):
    if request.method != "POST":
        return Http404("Request destination does not exist")

    id = request.POST['id']
    _pw = request.POST['password']
    pw = create_secret(_pw)

    user = User.objects.get(user_id=id, password=pw)
    if user is None:
        return Http404("Invalid User Data")

    request.session.clear()
    request.session['user_id'] = id
    request.session.modified = True

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/login')

def register(request):
    id = request.POST['id']
    _pw = request.POST['password']
    name = request.POST['name']

    find_user = User.objects.get(user_id = id)
    if find_user is not None:
        return Http404("User already exists.")

    user = User()

    user.user_id = id
    user.password = create_secret(_pw)
    user.name = name

    return HttpResponseRedirect('/login')
