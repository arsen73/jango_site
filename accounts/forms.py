from django.forms import ModelForm
from models import UserProfile

# Create the form class.
class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['gender', 'slug', 'avatar']