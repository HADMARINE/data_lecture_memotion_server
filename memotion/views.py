from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from django.template import loader


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


# def selectmemo(request, memo_id):
#     memo_list = get_object_or_404(Post, user_id)

