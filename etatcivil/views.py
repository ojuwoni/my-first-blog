from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms import layout, bootstrap
from .models import Bulletin, BirthCertificate, Registration, Country
from .forms import MessageForm, PersonForm #BulletinForm, RegistrationForm, BirthCertificateForm2, MessageForm

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render


#################################################
# Premièe page de l'application de l'etat civil #
# vue de connection de tout le projet           #
#################################################
# -*- coding: utf-8 -*-

class PersonCreate(CreateView):
        """
        Affichage du formulaire
        """
        model = Registration
        form_class = PersonForm
        success_url = reverse_lazy('etatcivil/success')

def person_success(request):
        return render(request, 'etatcivil/registration_success.html')



def debut(request):
    # This view is missing all form handling logic for simplicity of the example
	return render(request, 'etatcivil/index.html', {'form': MessageForm()})


#class PersonCreate(CreateView):
	"""
	Affichage du formulaire
	"""
#	model = Person
#	form_class = RegistrationForm
#	success_url = reverse_lazy('qslsldsdl')

#def registration_success(request):
#	return render(request, 'base.html')
