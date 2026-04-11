from django.db import models

class Entretien(models.Model):
    GUIDE_CHOICES = [
        ('mamans', 'Mamans'),
        ('sages_femmes', 'Sages-Femmes'),
        ('pharmaciens', 'Pharmaciens'),
    ]
    guide = models.CharField(max_length=20, choices=GUIDE_CHOICES)
    quartier = models.CharField(max_length=100, blank=True)
    date_entretien = models.CharField(max_length=20, blank=True)
    profil = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    score_motivation = models.IntegerField(null=True, blank=True)
    contact_whatsapp = models.CharField(max_length=20, blank=True)
    observations = models.TextField(blank=True)
    reponses = models.JSONField()  # toutes les réponses ici
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guide} — {self.quartier} — {self.created_at}"
