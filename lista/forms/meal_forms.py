from django import forms

from ..models import Meal, Mealingredient

class FilterMealForm(forms.ModelForm):
    search = forms.CharField(
        label='Busca por nombre', 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter para buscar'}))
    class Meta:
        model = Meal
        fields = ('search',)

class MealForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=200)
    islunch = forms.BooleanField(label='¿Es almuerzo?', required=False)
    ischecked = forms.BooleanField(label='¿Está marcado?', required=False)

    def clean_ischecked(self):
        data = self.cleaned_data['ischecked']
        return 1 if data == True else 0

    def clean_islunch(self):
        data = self.cleaned_data['islunch']
        return 1 if data == True else 0

    def __init__(self, *args, **kwargs):
        if kwargs.get('initial', None):
            if kwargs['initial']['ischecked']:
                del(kwargs['initial']['ischecked'])
        super().__init__(*args, **kwargs)
        self.fields['islunch'].initial = True if self.fields['islunch'] == 1 else False
        self.fields['ischecked'].initial = True if self.fields['ischecked'] == 1 else False
        self.fields['name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Meal
        fields = ('name', 'islunch', 'ischecked',)

class ChooseMealForm(forms.ModelForm):
    islunch = forms.BooleanField(
        label='',
        required=False)

    class Meta:
        model = Meal
        fields = ('islunch',)

class MealIngredientsForm(forms.ModelForm):
    ingredients = forms.JSONField()

    class Meta:
        model = Mealingredient
        fields = ('ingredients',)

class CheckMealForm(forms.ModelForm):
    ischecked = forms.BooleanField(
        label='',
        required=False)

    def clean_ischecked(self):
        data = self.cleaned_data['ischecked']
        return 1 if data == True else 0

    class Meta:
        model = Meal
        fields = ('ischecked',)