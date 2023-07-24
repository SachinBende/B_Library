from django import forms
from .models import Book

# creating a form
class GeeksForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	date_time = forms.DateTimeField()
	is_active = forms.BooleanField()
	price = forms.IntegerField()
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
	password = forms.CharField(widget = forms.PasswordInput())
	

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = "__all__"
		


STATES = (
    ('', 'Choose...'),
    ('MH', 'Maharastra'),
    ('MP', 'MadhyaPradesh'),
    ('UP', 'UttarPardesh')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': 'Manewada'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}) )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)        
