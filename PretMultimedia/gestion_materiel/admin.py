from django.contrib import admin
from .models import Enseignant, Salle, Equipement, Pret

class EquipementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'date_achat', 'cout', 'proprietaire')  # Colonnes affichées
    list_filter = ('type', 'proprietaire')  # Filtres disponibles
    search_fields = ('nom', 'type')  # Champs de recherche

# Enregistrer le modèle avec la configuration personnalisée
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Pret)