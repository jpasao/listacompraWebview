from django import forms

from ..models import Otherparent, Otherchild

class FilterOtherForm(forms.ModelForm):
    search = forms.CharField(
        label='Busca por nombre',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter para buscar'}))
    class Meta:
        model = Otherchild
        fields = ('search',)

class OtherForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=100)
    ischecked = forms.BooleanField(label='¿Está marcado?', required=False)
    parentid = forms.ModelChoiceField(
        queryset=Otherparent.objects.all().order_by('name'), 
        label='¿A qué lista pertenece?', 
        required=True)

    def clean_idchecked(self):
        data = self.cleaned_data['ischecked']
        return 1 if data == True else 0

    class Meta:
        model = Otherchild
        fields = ('name', 'ischecked', 'parentid',)

class CheckOtherForm(forms.ModelForm):
    ischecked = forms.BooleanField(
        label='',
        required=False)

    def clean_ischecked(self):
        data = self.cleaned_data['ischecked']
        return 1 if data == True else 0

    class Meta:
        model = Otherchild
        fields = ('ischecked',)

########## Other parent forms ##########

class FilterOtherParentForm(forms.ModelForm):
    search = forms.CharField(
        label='Busca por nombre',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter para buscar'}))
    class Meta:
        model = Otherparent
        fields = ('search',)

class OtherParentForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=50)

    class Meta:
        model = Otherparent
        fields = ('name',)