from django.db import models

class Patient(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    date_de_naissance = models.DateField(blank = True)
    adresse = models.CharField(max_length=255, blank = True)
    numero_de_telephone = models.CharField(max_length=20, blank = True)
    photo = models.ImageField(upload_to= "patient_image", blank= True, null=True)


    def __str__(self):
        return f"{self.nom} {self.prenom}"
class consultation(models.Model):
    id_patient = models.IntegerField()
    medicin_id = models.IntegerField()
    consultation_data = models.DateField()
    consultation_heure = models.TimeField()
    symptomes = models.TextField()
    diagnostic = models.TextField()
    commentaire = models.TextField()

