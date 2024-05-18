from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Equipement, Enseignant
from .forms import EquipementCreateForm
from django.urls import reverse_lazy

class EquipementListView(ListView):
    model = Equipement
    context_object_name = 'equipements'
    template_name = 'gestion_materiel/equipement_list.html'

class EnseignantListView(ListView):
    model = Enseignant
    context_object_name = 'enseignants'
    template_name = 'gestion_materiel/enseignant_list.html'

class EnseignantCreateView(CreateView):
    model = Enseignant
    fields = ['prenom', 'nom', 'email']
    template_name = 'gestion_materiel/enseignant_form.html'
    success_url = reverse_lazy('enseignant-list')

class EquipementDetailView(DetailView):
    model = Equipement
    context_object_name = 'equipement'
    template_name = 'gestion_materiel/equipement_detail.html'

class EquipementCreateView(CreateView):
    model = Equipement
    form_class = EquipementCreateForm
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

class EquipementUpdateView(UpdateView):
    model = Equipement
    fields = ['nom', 'type', 'date_achat', 'cout', 'type_budget', 'accessoires', 'etat_accessoires', 'acheteur', 'proprietaire', 'salle_actuelle', 'detenteur_actuel']
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

def home(request):
    return render(request, 'gestion_materiel/home.html')