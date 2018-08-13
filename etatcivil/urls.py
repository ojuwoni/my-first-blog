from django.conf.urls import url
from django.contrib import admin
from .views import PersonCreate,  person_success #, DeclarationBirth, DeclarationSuccess
from . import views

urlpatterns = [
#    url(r'^$', views.debut),
    url(r'^$', PersonCreate.as_view(), name='add'),
    url(r'^success/$', person_success, name='success'),
#    url(r'^nouveau$', DeclarationBirth.as_view(), name='naissance'),
 #   url(r'^birthsuccess/$', DeclarationSuccess, name='birthsuccess'),
#    url(r'^CreatePlug/$', views.CreatePlug, name='CretePlug'),
#    url(r'^ViewPlug/$', views.ViewPlug, name='ViewPlug'),
]
