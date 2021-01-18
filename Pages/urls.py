from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('models',views.models,name='models'),
    path('tutorial',views.tutorial,name='tutorial'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    #path('accounts/', include('allauth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)