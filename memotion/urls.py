from django.urls import path

from memotion.views import logout, login, get_post

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('post/<int:post_id>/view', get_post),
]