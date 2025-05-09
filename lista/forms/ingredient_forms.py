from django import forms

from ..models import Ingredient

class FilterIngredientForm(forms.ModelForm):
    search = forms.CharField(
        label='Busca por nombre o comentario', 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter para buscar'}))
    class Meta:
        model = Ingredient
        fields = ('search',)

class CheckIngredientForm(forms.ModelForm):
    ischecked = forms.BooleanField(
        label='', 
        required=False)

    def clean_ischecked(self):
        data = self.cleaned_data['ischecked']
        return "1" if data == True else "0"

    class Meta:
        model = Ingredient
        fields = ('ischecked',)

class QuantityIngredientForm(forms.ModelForm):
    quantityChanged = forms.IntegerField(
        label='', 
        required=False)

    class Meta:
        model = Ingredient
        fields = ('quantityChanged',)

class IngredientForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=200)
    ischecked = forms.BooleanField(label='¿Está marcado?', required=False)
    quantity = forms.IntegerField(label='Cantidad', required=False)
    comment = forms.CharField(widget=forms.Textarea, label='Comentarios', required=False)

    def clean_ischecked(self):
        data = self.cleaned_data['ischecked']
        return "1" if data == True else "0"
    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        return 1 if data == None else data
    def __init__(self, *args, **kwargs):
        if kwargs.get('initial', None):
            if kwargs['initial']['ischecked']:
                del(kwargs['initial']['ischecked'])
        super().__init__(*args, **kwargs)
        self.fields['ischecked'].initial = True if self.fields['ischecked'] == '1' else False
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Ingredient
        fields = ('name', 'ischecked', 'quantity', 'comment',)