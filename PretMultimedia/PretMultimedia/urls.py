from django.contrib import admin
from django.urls import path
from gestion_materiel.views import home, EnseignantListView, EquipementListView, EnseignantCreateView, EquipementDetailView, EquipementCreateView, EquipementUpdateView

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('equipements/', EquipementListView.as_view(), name='equipement-list'),
    path('enseignants/', EnseignantListView.as_view(), name='enseignant-list'),
    path('enseignants/new/', EnseignantCreateView.as_view(), name='enseignant-create'),
    path('equipements/<int:pk>/', EquipementDetailView.as_view(), name='equipement-detail'),
    path('equipements/new/', EquipementCreateView.as_view(), name='equipement-create'),
    path('equipements/<int:pk>/edit/', EquipementUpdateView.as_view(), name='equipement-update'),
]