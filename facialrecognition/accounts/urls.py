from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url(r'^logout/$', LoginView.as_view(template_name='accounts/logout.html'), name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^loggedin/$', LoginView.as_view(template_name='accounts/loggedIn.html'), name="loggedin"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)