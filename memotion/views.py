import datetime
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

    try:
        # memo_list = Memo.objects.get(user=user_id).order_by('-pub_date')
        memo_list = Memo.objects.filter(user_id=user_id).order_by('-pub_date')
    except:
        memo_list = None

    user = User.objects.get(pk=user_id)
    context = {'memo_list': memo_list, 'user': user}
    return render(request, 'memotion/index_page.html', context)


def get_memo(request, memo_id):
    user_id = request.session.get('user_id', None)
    if user_id is None:
        return HttpResponseRedirect('/login')

    selected_memo = Memo.objects.get(id=memo_id)
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
    id = request.session.get('user_id', None)

    if id == None:
        return HttpResponseRedirect("/login")

    user = User.objects.get(user_id=id)

    memo = Memo()
    memo.user = user
    memo.title = ""
    memo.content = ""
    memo.pub_date = datetime.datetime.now()
    memo.save()

    return render(request, 'memotion/memo.html', {'selected_memo': memo})


def delete_memo(request, memo_id):
    Memo.objects.filter(pk=memo_id).delete()
    return HttpResponseRedirect(reverse('memotion:index_page', args=()))

def login_page(request):
    return render(request, 'memotion/login.html')

def login(request):
    if request.method != "POST":
        return Http404("Request destination does not exist")

    id = request.POST['user_id']
    _pw = request.POST['password']
    pw = _pw

    user = None

    try:
        user = User.objects.get(user_id=id)
    except:
        return HttpResponseRedirect("/login")

    if user is None:
        return HttpResponse("USER NOT FOUND")

    if user.password != _pw:
        return HttpResponse("PASSWORD INVALID")

    request.session.clear()
    request.session['user_id'] = id
    request.session.modified = True

    return HttpResponseRedirect('/')

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/login')

def register_page(request):
    return render(request, 'memotion/register.html')

def register(request):
    id = request.POST['user_id']
    _pw = request.POST['password']
    name = request.POST['name']

    # find_user = User.objects.get(pk=id)
    #
    # if find_user is not None:
    #     return HttpResponse("User already exists.")

    user = User()

    user.user_id = id
    user.password = _pw
    user.name = name

    user.save()

    return HttpResponseRedirect('/login')
