from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser

COUNTRY = [
    ('India', 'India'),
    ('USA', 'USA'),
    ('UK', 'UK')
]

DIET = [
    ('Heavy_Meat_Eater', 'Heavy_Meat'),
    ('Medium_Meat_Eater', 'Low_Meat'),
    ('Low_Meat_Eater', 'Low_Meat'),
    ('Vegetarian', 'Vegeterian'),
    ('Vegan', 'Vegan')
]

FUEL = [
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Other', 'Other')
]

ELECTRICITY = [
    ('One-Three', 'One to Three hours'),
    ('Three-Five', 'Three to Five hours'),
    ('Six-Above', 'Above Six Hours')
]


class SignUpForm(UserCreationForm, forms.ModelForm):
    country = forms.ChoiceField(choices=COUNTRY, widget=forms.RadioSelect())
    diet = forms.ChoiceField(choices=DIET, widget=forms.RadioSelect())
    fuel = forms.ChoiceField(choices=FUEL, widget=forms.RadioSelect())
    electricity = forms.ChoiceField(choices=ELECTRICITY, widget=forms.RadioSelect())

    class Meta:
        model = MyUser
        fields = ('email', 'name', 'age', 'country', 'diet', 'fuel', 'scooter', 'family', 'electricity')
