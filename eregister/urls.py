from django.conf.urls import url, include
from django.contrib import admin
from . import views

appName = "eregister"
urlpatterns = [
    url(r'^admin/', 		admin.site.urls),
    url('', 	include('dev.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
