from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
	"""docstring for RegistrationForm"""
	email = forms.EmailField(required=True)

	class Meta: # define a metadata related to this class
		model = User
		fields = (
			'username',
			'email',
			'password1',
			'password2',

		)

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = [
			'image',
			'date_of_birth',
		]

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
		]