from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    # path('<str:user_id>/', views.memolist, name='memolist'),
    # path('<str:user_id>/<int:id>/', views.memo, name='memo')

    path('', views.index_page, name='index_page'),
    path('memo/<int:memo_id>/save', views.save_memo, name='save_memo'),
    path('memo/<int:memo_id>/view', views.get_memo, name='show_memo'),
    path('<int:memo_id>/delete', views.delete_memo, name='delete_memo'),
    path('memo/create', views.create_memo, name="memo_create"),
    path('login/', views.login_page, name="login_page"),
    path('api/login/', views.login, name="login"),
    path('register/', views.register_page, name="register_page"),
    path('api/register/', views.register, name="register"),
    path('logout/', views.logout),
]

app_name = 'memotion'
