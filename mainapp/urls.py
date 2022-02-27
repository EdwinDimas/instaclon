from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('profile', views.profile, name = "profile"),
    path('post/new', views.newPost, name = "newpost"),
    path('post/like', views.handleLike, name = "newlike")
    
] 

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)