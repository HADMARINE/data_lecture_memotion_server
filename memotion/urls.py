from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    # path('<str:user_id>/', views.memolist, name='memolist'),
    # path('<str:user_id>/<int:id>/', views.memo, name='memo')

    path('', views.memoindex, name='memoindex'),
    path('<int:memo_id>/save', views.savememo, name='savememo'),
    path('<int:memo_id>/', views.showmemo, name='memo')
]

app_name = 'memotion'
