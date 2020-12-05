import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.


from memotion.models import Memo


# def login(request):
#     context = {'user_id': user_id}
#     return render(request, 'memotion/login.html')


def memoindex(request):
    memo_list = Memo.objects.all().order_by('-pub_date')
    context = {'memo_list': memo_list}
    return render(request, 'memotion/memoindex.html', context)


def showmemo(request, memo_id):
    selected_memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memotion/memo.html', {'selected_memo': selected_memo})


def savememo(request, memo_id):
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
    return HttpResponseRedirect(reverse('memotion:memoindex', args=()))


def newmemo(request):
    memo = Memo()
    memo.title = ""
    memo.content = ""
    memo.pub_date = datetime.datetime.now()
    memo.save()
    return render(request, 'memotion/memo.html', {'selected_memo': memo})


def deletememo(request, memo_id):
    Memo.objects.filter(pk=memo_id).delete()
    return HttpResponseRedirect(reverse('memotion:memoindex', args=()))

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