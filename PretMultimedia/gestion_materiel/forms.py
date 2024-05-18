from django import forms
from .models import Equipement, Enseignant, Salle

class EquipementCreateForm(forms.ModelForm):
    proprietaire = forms.ModelChoiceField(queryset=Enseignant.objects.all(), required=False)
    detenteur_actuel = forms.ModelChoiceField(queryset=Enseignant.objects.all(), required=False)

    salle_default = Salle.objects.get(numero_salle="001", numero_etage=0)
    salle_actuelle = forms.ModelChoiceField(queryset=Salle.objects.all(), initial=salle_default)

    etat_accessoires = forms.ChoiceField(choices=[('Neuf', 'Neuf'), ('Bon Etat', 'Bon Etat'), ('Usée', 'Usée'), ('Manquant', 'Manquant')])

    type_budget = forms.CharField(widget=forms.TextInput(attrs={'list':'budgets'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'list':'types'}))

    class Meta:
        model = Equipement
        fields = ['nom', 'type', 'date_achat', 'cout', 'type_budget', 'accessoires', 'etat_accessoires', 'acheteur', 'proprietaire', 'salle_actuelle', 'detenteur_actuel']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'date_achat': forms.DateInput(attrs={'type': 'date', 'class': 'my-custom-class'}),
            'cout': forms.NumberInput(attrs={'class': 'my-custom-class'}),
            'accessoires': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'acheteur': forms.Select(attrs={'class': 'my-custom-class'}),
            'proprietaire': forms.Select(attrs={'class': 'my-custom-class'}),
            'salle_actuelle': forms.Select(attrs={'class': 'my-custom-class'}),
            'detenteur_actuel': forms.Select(attrs={'class': 'my-custom-class'}),
        } 

class EquipementUpdateForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = ['nom', 'type', 'date_achat', 'cout', 'type_budget', 'accessoires', 'etat_accessoires', 'acheteur', 'proprietaire', 'salle_actuelle', 'detenteur_actuel']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'type': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'date_achat': forms.DateInput(attrs={'type': 'date', 'class': 'my-custom-class'}),
            'cout': forms.NumberInput(attrs={'class': 'my-custom-class'}),
            'type_budget': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'accessoires': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'etat_accessoires': forms.TextInput(attrs={'class': 'my-custom-class'}),
            'acheteur': forms.Select(attrs={'class': 'my-custom-class'}),
            'proprietaire': forms.Select(attrs={'class': 'my-custom-class'}),
            'salle_actuelle': forms.Select(attrs={'class': 'my-custom-class'}),
            'detenteur_actuel': forms.Select(attrs={'class': 'my-custom-class'}),
        } 
