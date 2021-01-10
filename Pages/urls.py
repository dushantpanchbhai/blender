from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('models',views.models,name='models'),
    path('tutorial',views.tutorial,name='tutorial'),
    path('login',views.login,name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)