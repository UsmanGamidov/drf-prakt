from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreatoanForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User



