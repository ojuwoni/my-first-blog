# -*- coding: utf-8 -*-
from django import forms
from crispy_forms import layout, bootstrap

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions,  StrictButton,TabHolder, Tab
from bootstrap3_datetime.widgets import DateTimePicker
from .models import Identity, Supervisor, BirthCertificate, Bulletin, Registration
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import ugettext_lazy as _, ugettext



class MessageForm(forms.Form):
    text_input = forms.CharField()

    textarea = forms.CharField(
        widget = forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"), 
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"), 
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text = "Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('text_input', css_class='input-xlarge'),
        Field('textarea', rows="3", css_class='input-xlarge'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
)







class PersonForm(forms.ModelForm):
	"""
	Formulaire d'inscription
	"""

	# Ici, tu vas rajouter les champs supplémentaires au modèle
	# Tu définis le captcha
	#captcha = CaptchaField()
	# Tu ajoutes un mail de confirmation
	confirmation_mail = forms.EmailField(label="Mail de confirmation")

	def __init__(self, *args, **kwargs):
		"""
		Surcharge de l'initialisation du formulaire
		"""
		super().__init__(*args, **kwargs)
		# Tu modifies le label de la date de naissance pour rajouter le format
		self.fields['birthday'].label = "%s (JJ/MM/AAAA)" % "Date de naissance"
		# Tu utilises FormHelper pour customiser ton formulaire
		self.helper = FormHelper()
		# Tu définis l'id et la classe bootstrap de ton formulaire
		self.helper.form_class = 'form-horizontal'
		self.helper.form_id = 'Person-form'
		# Tu définis la taille des labels et des champs sur la grille
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-8'
		# Tu crées l'affichage de ton formulaire
		self.helper.layout = Layout(
			# Le formulaire va contenir 3 onglets
			TabHolder(
			# Premier onglet
			Tab(
			# Label de l'onglet
			'Étape 1 - Identité',
			# Liste des champs du modèle à afficher dans l'onglet
			'title',
			'lastname',
			'firstname',
			'young_girl_lastname',
			'birthday',
			'birthcity',
			'nationality',
			# Tu rajoutes un bouton "Suivant"
			StrictButton(
			'<span class="glyphicon glyphicon-arrow-right" \
			aria-hidden="true"></span> %s' % "Suivant",
			type='button',
			css_class='btn-default col-md-offset-9 btnNext',
			)

			),
			# Deuxième onglet
			Tab(
			# Label de l'onglet
			'Étape 2 - Adresse',
			# Liste des champs à afficher
			'address',
			'city',
			'borough',
			'district',
			'islet',
			'plot',
			'phone',
			# Tu rajoutes des boutons "Précédent" et "Suivant"
			StrictButton(
			'<span class="glyphicon glyphicon-arrow-left" \
			aria-hidden="true"></span> %s' % 'Précédent',
			type='button',
			css_class='btn-default btnPrevious',
			),
			StrictButton(
			'<span class="glyphicon glyphicon-arrow-right" \
			aria-hidden="true"></span> %s' % 'Suivant',
			type='button',
			css_class='btn-default col-md-offset-8 btnNext',
			)
			),
			# Troisième onglet
			Tab(
			# Label de l'onglet
			'Étape 3 - Validation',
			# Liste des champs à afficher dont les champs supplémentaires
			'mail',
			'confirmation_mail',
			'comments',
			# Tu rajoutes des boutons "Précédent" et "Valider"
			StrictButton(
			'<span class="glyphicon glyphicon-arrow-left" \
			aria-hidden="true"></span> %s' % "Précédent",
			type='button',
			css_class='btn-default btnPrevious',
			),
			StrictButton(
			'<span class="glyphicon glyphicon-ok" \
			aria-hidden="true"></span> %s' % "Valider",
			type='submit',
			css_class='btn-default col-md-offset-8'
			)
			),
		),
	)
	class Meta:
		# Tu définis le modèle utilisé
		model = Registration
		fields = ['title', 'lastname', 'firstname', 'young_girl_lastname', 'sex', 'birthday', 'birthcity',
		'nationality', 'address', 'city', 'borough', 'district', 'islet', 'plot', 'phone', 'mail','comments']

		# Tu customises le champ date de naissance pour ajouter le date picker
		widgets = {
		'birthday': DateTimePicker(
		options={"format": "DD/MM/YYYY", "pickTime": False,
		"useStrict": True, "viewMode": "years",
		"startDate": "01/01/1900"},
		attrs={'placeholder': 'ex: 05/11/1975'}
		)
		}
