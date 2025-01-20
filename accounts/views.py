from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import RegistrationForm, UserUpdateForm, ProfileForm
from accounts.models import Profile


# Create your views here.
@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'pages/user_profile.html', context)

class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'


    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        return HttpResponseRedirect(self.success_url)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pages/user_profile_edit.html'

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            return redirect(reverse_lazy('profile'))  # redirect ishlatildi

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)
