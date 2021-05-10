from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# appname ='artistly'

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('models',views.models,name='models'),
    path('tutorial',views.tutorial,name='tutorial'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addmodel',views.addmodel,name='addmodel'),
    path('addvideo',views.addvideo,name='addvideo'),
    path('feedback',views.feedback,name='feedback'),
    path('help',views.help,name='help'),
    path('analytics',views.analytics,name='analytics'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)