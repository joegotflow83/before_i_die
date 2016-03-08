from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import ProfileUserForm
from .models import UserProfile


class Signup(CreateView):
    """Allow a user to signup"""
    model = User
    form_class = ProfileUserForm

    def form_valid(self, form):
        """Validate the form"""
        user_object = form.save()
        UserProfile.objects.create(user=user_object,
                                   first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   origin=form.cleaned_data['origin'],
                                   dream_location=form.cleaned_data['dream_location'],
                                   age=form.cleaned_data['age'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
