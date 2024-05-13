from django.db import models

class Enseignant(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Salle(models.Model):
    numero_salle = models.CharField(max_length=10)
    numero_etage = models.IntegerField()

    def __str__(self):
        return f"Salle {self.numero_salle} à l'étage {self.numero_etage}"

class Equipement(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date_achat = models.DateField()
    cout = models.DecimalField(max_digits=8, decimal_places=2)
    type_budget = models.CharField(max_length=100)  # Type de budget utilisé pour l'achat
    accessoires = models.CharField(max_length=200)  # Liste des accessoires
    etat_accessoires = models.CharField(max_length=200)  # État des accessoires
    proprietaire = models.ForeignKey(Enseignant, related_name='equipements_possedes', on_delete=models.SET_NULL, null=True)
    salle_actuelle = models.ForeignKey(Salle, related_name='equipements_stockes', on_delete=models.SET_NULL, null=True)
    detenteur_actuel = models.ForeignKey(Enseignant, related_name='equipements_detenus', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Pret(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Enseignant, related_name='prets', on_delete=models.CASCADE)
    date_pret = models.DateField()
    date_retour = models.DateField(null=True, blank=True)
    lieu_pret = models.CharField(max_length=100)  # Lieu du prêt
    objectif_utilisation = models.CharField(max_length=200)  # Objectif de l'utilisation

    def __str__(self):
        return f"{self.equipement.nom} prêté à {self.emprunteur}"
