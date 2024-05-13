from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Equipement, Enseignant
from django.urls import reverse_lazy

class EquipementListView(ListView):
    model = Equipement
    context_object_name = 'equipements'
    template_name = 'gestion_materiel/equipement_list.html'

class EnseignantListView(ListView):
    model = Enseignant
    context_object_name = 'enseignants'
    template_name = 'gestion_materiel/enseignant_list.html'

class EquipementDetailView(DetailView):
    model = Equipement
    context_object_name = 'equipement'
    template_name = 'gestion_materiel/equipement_detail.html'

class EquipementCreateView(CreateView):
    model = Equipement
    fields = ['nom', 'type', 'date_achat', 'cout', 'type_budget', 'accessoires', 'etat_accessoires', 'proprietaire', 'salle_actuelle', 'detenteur_actuel']
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

class EquipementUpdateView(UpdateView):
    model = Equipement
    fields = ['nom', 'type', 'date_achat', 'cout', 'type_budget', 'accessoires', 'etat_accessoires', 'proprietaire', 'salle_actuelle', 'detenteur_actuel']
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

def home(request):
    return render(request, 'gestion_materiel/home.html')