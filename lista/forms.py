from django import forms

from .models import Author, Ingredient

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'image',)

class FilterIngredientForm(forms.ModelForm):
    search = forms.CharField(
        label='Busca por nombre o comentario', 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter para buscar'})
        )
    class Meta:
        model = Ingredient
        fields = ('search',)

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

    class Meta:
        model = Ingredient
        fields = ('name', 'ischecked', 'quantity', 'comment',)