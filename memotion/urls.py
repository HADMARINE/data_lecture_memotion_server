from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    # path('<str:user_id>/', views.memolist, name='memolist'),
    # path('<str:user_id>/<int:id>/', views.memo, name='memo')

    path('', views.memoindex, name='index_page'),
    path('memo/<int:memo_id>/save', views.savememo, name='save_memo'),
    path('memo/<int:memo_id>/view', views.showmemo, name='show_memo'),
    path('<int:memo_id>/delete', views.deletememo, name='delete_memo'),
    path('newmemo/', views.newmemo, name="memo_create"),
    path('login/', login),
    path('logout/', logout),
]

app_name = 'memotion'
