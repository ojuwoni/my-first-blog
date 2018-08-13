from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


###################################################
# Création d'une table répertoriant tous les pays #
###################################################
 
class Country(models.Model):
 
	code = models.CharField(max_length=3, null=False)  # Example : 'FR' - 'US'
	pays = models.CharField(max_length=50, null=False)  # Example : 'France' - 'Etats-Unis'
 
	def __self__(self):
		return '%s %s %s' % (self.id, self.code, self.pays)

STATUT=(
	('V','Vivant'),
	('D','Décédé'),
	('I','Disparu')
	)

STATUS_CHOICES=(
	('C','Célibataire'),
	('M','Marié'),
	('V','Veuf')
	)


######################################
# Choix à l'utilisateur pour le sexe # 
###################################### 
SEX_CHOICES = (
    ('M', 'Mâle'),
    ('F', 'Femelle')
)
##########################################
# Choix à l'utilisateur pour la civilité #
##########################################
 
TITLE_CHOICES = (
    ('Mr', 'Monsieur'),
    ('Mlle', 'Mademoiselle'),
    ('Mme','Madame'),
    ('Dr','Docteur'),
    ('Me','Maître'),
)
####################################################################################
# Création d'une table permettant de renseigner toutes les informations concernant #
# le profil des utilisateurs 				                           #
#s###################################################################################
class UserProfile(models.Model):
	name		= models.CharField(max_length=50, verbose_name="Name")
	login		= models.CharField(max_length=25, verbose_name="Login")
	password	= models.CharField(max_length=100, verbose_name="Password")
	phone		= models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
	born_date	= models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
	last_connection	= models.DateField(verbose_name="date of last connection", null=True, default=None, blank=True)
	email		= models.EmailField(verbose_name="Email")
	years_seniority	= models.IntegerField(verbose_name="Seniority", default=0)
	date_created	= models.DateField(verbose_name="Date of birthday", auto_now_add=True)

	def __str__(self):
		return self.name

#####################################################################################
# Table definissant toutes les applications auxquelles l'utilisateur se connect     #
#####################################################################################
class Project(models.Model):
	title 		= models.CharField(max_length=50, verbose_name = "Title")
	description	= models.CharField(max_length=1000, verbose_name="Description")
	client_name	= models.CharField(max_length=1000, verbose_name="Client name")


###################################################################################
class Supervisor(UserProfile):
	specialisation	= models.CharField(max_length=50, verbose_name="Specialisation")

class Developer(UserProfile):
	supervisor_field	= models.ForeignKey(Supervisor, verbose_name="Supervisor", on_delete=models.CASCADE)


#####################################################################################
# Table definissant les tâches accomplies par un utilisateur                        #
#####################################################################################
class Task(models.Model):
	title		= models.CharField(max_length=50, verbose_name="Title")
	description	= models.CharField(max_length=1000, verbose_name="Description")
	time_elapsed	= models.IntegerField(verbose_name="Elapsed tiem", null=True, default=None, blank=True)
	importance	= models.IntegerField(verbose_name="Importance")
	project		= models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True, on_delete=models.CASCADE)
	developer	= models.ForeignKey(Developer, verbose_name="User", on_delete=models.CASCADE)



####################################################################################
# Création d'une table permettant de renseigner toutes les informations concernant #
#                les parents et reprise de celles des enfants                      #
####################################################################################
 
class Identity(models.Model):
 
    
	lastname = models.CharField(max_length=30, verbose_name='Nom de famille')
	firstname = models.CharField(max_length=30, verbose_name='Prénom(s)')
 
	def __str__(self):
		return '%s %s' % (self.lastname, self.firstname)




# La classe Naissance
class Naissances(models.Model):
#	nip   			= models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Numéro d'identification")
	nip   			= models.OneToOneField('Registration', on_delete=models.CASCADE)
	num_cert 		= models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Numéro du certificat de naissance")
	poids			= models.DecimalField(max_digits=4,  decimal_places=2, verbose_name="Poids à la naissance")
	lieu_residence		= models.CharField(max_length=50, verbose_name="Lieu de résidence de la mère")
	personne_ass_accouchee  = models.CharField(max_length=50, verbose_name="Personne ayant assistée l'accouchée")
	lieu_naissance 		= models.CharField(max_length=50)
	date_naissance 		= models.DateTimeField(default=timezone.now,verbose_name="Date de naissance")
	date_enregistrement 	= models.DateTimeField(default=timezone.now,verbose_name="Date d'enregistrement")
	#       categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

	def __str__(self):
		"""
		Cette méthode que nous définirons dans tous les modèles
		nous permettra de reconnaître facilement les différents objets
		que nous traiterons plus tard dans l'administration
		"""
		return str(self.nip)

class Registration(models.Model):

	CIVILITY_CHOICES=(
		('M.', 'M.'),
		('MME', 'Mme')
		)

	STREET_TYPE_CHOICES = (
		('Boulevard', 'Boulevard'),
		('Avenue', 'Avenue'),
		('Cours', 'Cours'),
		('Place', 'Place'),
		('Rue', 'Rue'),
		('Route', 'Route'),
		('Voie', 'Voie'),
		)
	title                       = models.CharField(max_length=3, choices=CIVILITY_CHOICES,
						 default='M.', verbose_name="Civilité")
	lastname		    =  models.CharField(max_length=255, verbose_name='Nom')
	young_girl_lastname         = models.CharField(max_length=30, verbose_name='Nom de jeune fille', blank=True)
	firstname                   = models.CharField(max_length=255, verbose_name='Prénom')
	status                      = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='Stuation matrimoniale')
	sex                         = models.CharField(max_length=8, choices=SEX_CHOICES, verbose_name='Sexe')
	birthday                   = models.DateField(verbose_name='Date de naissance')
	birthcity                   = models.CharField(max_length=255, verbose_name='Ville de naissance')
	nationality                 = CountryField(max_length=255, verbose_name='Pays de naissance')
	job                         = models.CharField(max_length=30, verbose_name='Profession')
	address                     = models.CharField(max_length=30, verbose_name='Adresse')
	city                        = models.CharField(max_length=255, verbose_name='Ville de résidence')
	borough                     = models.CharField(max_length=30, verbose_name='Arrondissement')
	district                    = models.CharField(max_length=30, verbose_name='Quartier')
	islet                       = models.CharField(max_length=30, verbose_name='Îlot')
	plot                        = models.CharField(max_length=30, verbose_name='Parcelle')
	phone                       = models.CharField(max_length=255, blank=True, null=True, verbose_name='Téléphone')
	mail                        = models.EmailField(max_length=255, verbose_name='Mail')
	created			    = models.DateTimeField(auto_now_add=True)
	comments                    = models.TextField(blank=True, null=True, verbose_name='Commentaires')

	def __unicode__(self):
		return self.lastname


class BirthCertificate(Registration):
     
	num_cert                = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Numéro du certificat de naissance")
	poids                   = models.DecimalField(max_digits=4,  decimal_places=2, verbose_name="Poids à la naissance")
	personne_ass_accouchee  = models.CharField(max_length=50, verbose_name="Personne ayant assistée l'accouchée")
	birthour 		= models.TimeField(null=True, verbose_name='Heure de naissance')
	fk_parent1 		= models.ForeignKey(Registration, related_name='ID_Parent1', verbose_name='ID parent1', null=False)
	fk_parent2 		= models.ForeignKey(Registration, related_name='ID_Parent2', verbose_name='ID parent2', null=False)
	mairie 			= models.CharField(max_length=30, null=False, verbose_name='Mairie')





	def __str__(self):
                """
                Cette méthode que nous définirons dans tous les modèles
                nous permettra de reconnaître facilement les différents objets
                que nous traiterons plus tard dans l'administration
                """
                return str(self.nip)

class Hommes(Registration):
#	nip_homme		= models.OneToOneField('Personnes', on_delete=models.CASCADE)

	def __str__(self):
		super().__str__()
		self.sexe	= "M"
		return self.nom


class Femmes(Registration):

	def __str__(self):
		super().__str__()
		super().sexe	= "Femme"
		return self.nom

class Deces(models.Model):
	#nip			= models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Numéro d'identification de la personne")
	nip			= models.OneToOneField('Registration', on_delete=models.CASCADE)
	date			= models.DateTimeField(default=timezone.now,verbose_name="Date du décès")
	lieu			= models.CharField(max_length=100, verbose_name="lieu de décès")
	date_enreg		= models.DateTimeField(default=timezone.now,verbose_name="Date de l'enregistrement")
	cause			= models.CharField(max_length=100, verbose_name="cause du décès")
	auteur_certif		= models.CharField(max_length=30, verbose_name="Auteur du certificat")
	num_certif		= models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Numéro du certificat de décès")
	residence		= models.CharField(max_length=50, verbose_name="lieu de résidence habituelle du défun")
	residence_mere		= models.CharField(max_length=50, verbose_name="lieu de résidence habituelle de la mère pour enfants moin d'un an")

	def __str__(self):
                """
                Cette méthode que nous définirons dans tous les modèles
                nous permettra de reconnaître facilement les différents objets
                que nous traiterons plus tard dans l'administration
                """
                return self.nip

class MortsFoetales(models.Model):
	nip_mere		= models.DecimalField(max_digits=8, decimal_places=0, 
					verbose_name="Numéro d'identification de la mère")






TYPE_CHOICES = (
	('searching', _("Searching")),
	('offering', _("Offering")),
	)
class Bulletin(models.Model):
	bulletin_type = models.CharField(_("Type"), max_length=20,  choices=TYPE_CHOICES)
	title = models.CharField(_("Title"), max_length=255)
	description = models.TextField(_("Description"), max_length=300)
	contact_person = models.CharField(_("Contact person"), max_length=255)
	phone = models.CharField(_("Phone"), max_length=200,  blank=True)
	email = models.EmailField(_("Email"), blank=True)
	image = models.ImageField(_("Image"), max_length=255, upload_to="bulletin_board/", blank=True)

	class Meta:
		verbose_name = _("Bulletin")
		verbose_name_plural = _("Bulletins")
		ordering = ("title",)
	def __unicode__(self):
		return self.title




