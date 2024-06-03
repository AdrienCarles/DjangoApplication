from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Equipement, Enseignant, Pret
from .forms import EquipementCreateForm, EquipementUpdateForm, PretCreateForm
from django.urls import reverse_lazy

class EnseignantListView(ListView):
    model = Enseignant
    context_object_name = 'enseignants'
    template_name = 'gestion_materiel/enseignant_list.html'

class EnseignantCreateView(CreateView):
    model = Enseignant
    fields = ['prenom', 'nom', 'email']
    template_name = 'gestion_materiel/enseignant_form.html'
    success_url = reverse_lazy('enseignant-list')

class EnseignantDetailView(DetailView):
    model = Enseignant
    context_object_name = 'enseignant'
    template_name = 'gestion_materiel/enseignant_detail.html'

class EquipementListView(ListView):
    model = Equipement
    context_object_name = 'equipements'
    template_name = 'gestion_materiel/equipement_list.html'

class EquipementCreateView(CreateView):
    model = Equipement
    form_class = EquipementCreateForm
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

class EquipementDetailView(DetailView):
    model = Equipement
    context_object_name = 'equipement'
    template_name = 'gestion_materiel/equipement_detail.html'

class EquipementUpdateView(UpdateView):
    model = Equipement
    form_class = EquipementUpdateForm
    template_name = 'gestion_materiel/equipement_form.html'
    success_url = reverse_lazy('equipement-list')

class PretListView(ListView):
    model = Pret
    context_object_name = 'prets'
    template_name = 'gestion_materiel/pret_list.html'

class PretCreateView(CreateView):
    model = Pret
    form_class = PretCreateForm
    template_name = 'gestion_materiel/pret_form.html'
    success_url = reverse_lazy('pret-list')

def home(request):
    return render(request, 'gestion_materiel/home.html')