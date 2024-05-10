from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    
    def set_mot_de_passe(self, mot_de_passe):
        self.password = make_password(mot_de_passe)
    
    def verifier_password(self, mot_de_passe):
        verification = check_password(mot_de_passe)
        return verification
        
        
class Document(models.Model):
    primata = 'primata'
    duplicatatUse = 'duplicatatUse'
    duplicatatPerte = 'duplicatatPerte'

    TYPE_DOCUMENT = [
        (primata, 'primata'),
        (duplicatatUse, 'duplicatatUse'),
        (duplicatatPerte, 'duplicatatPerte'),
    ]
    
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    numCni = models.CharField(max_length=9, blank=True)
    photo =  models.ImageField(upload_to='backend/image/photo')
    declarationPerte = models.ImageField(upload_to='backend/image/perte',blank=True)
    certificat = models.ImageField(upload_to='backend/image/certificat')
    acteNaissance = models.ImageField(upload_to='backend/image/acte',default="",blank=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    typeDocument = models.CharField(max_length=20, choices=TYPE_DOCUMENT, default=primata)
    
