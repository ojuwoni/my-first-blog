from django import forms
from .models import Personnes, Identity, Supervisor



class IdentityForm(forms.ModelForm) :
 
    class Meta :
        model = Identity
        fields = '__all__'




class PersonForm(forms.ModelForm):
	
	lastname	= forms.CharField(max_length=50)
	firstname	= forms.CharField(max_length=50)
	status		= forms.CharField(max_length=50)
	sex		= forms.CharField(max_length=1)
	

	class Meta:
		model		= Person
		fields		= '__all__'

	def __str__(self):
		return '%s %s %s %s %s' % (self.nom, self.prenom, self.situation, self.sexe, self.situation_mat)



class FormInscription(forms.Form):
	# This line creates the form with four fields. It is an object that
	#inherits from forms.Form. It contains attributes that define the form fields.
	name = forms.CharField(label="Name", max_length=30)
	login = forms.CharField(label="Login", max_length=30)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())
# View for create_developer
