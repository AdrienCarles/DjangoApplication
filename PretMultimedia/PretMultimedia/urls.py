from django.contrib import admin
from django.urls import path
from gestion_materiel.views import home, EnseignantListView, EquipementListView, EnseignantDetailView, EnseignantCreateView, EquipementDetailView, EquipementCreateView, EquipementUpdateView, PretListView, PretCreateView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('enseignants/', EnseignantListView.as_view(), name='enseignant-list'),
    path('enseignants/new/', EnseignantCreateView.as_view(), name='enseignant-create'),
    path('enseignants/<int:pk>/', EnseignantDetailView.as_view(), name='enseignant-detail'),
    path('equipements/', EquipementListView.as_view(), name='equipement-list'),
    path('equipements/new/', EquipementCreateView.as_view(), name='equipement-create'),
    path('equipements/<int:pk>/', EquipementDetailView.as_view(), name='equipement-detail'),
    path('equipements/<int:pk>/edit/', EquipementUpdateView.as_view(), name='equipement-update'),
    path('prets/', PretListView.as_view(), name='pret-list'),
    path('prets/new/', PretCreateView.as_view(), name='pret-create'),
]