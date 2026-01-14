from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import LoginForm, ProfileUpdateForm, UserRegisterForm, ProfileRegisterForm
from .models import UserProfile

# Create your views here.
class RegisterView(View):
    template_name = "auth_system/register.html"
    success_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
        context = {
            "user_form": user_form,
            "profile_form": profile_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
        return render(request, self.template_name, {
            "user_form": user_form,
            "profile_form": profile_form
        })

class UserLoginView(LoginView):
    template_name = "auth_system/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("profile")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# class UsersListView(LoginRequiredMixin,  ListView):
#     model = CustomUser
#     template_name = "auth_system/users_list.html"


# class ProfileView(LoginRequiredMixin, DetailView):
#     model = CustomUser
#     template_name = ("auth_system/profile.html")
#     context_object_name = 'user'

#     def get_object(self):
#         return self.request.user

# class ProfileEditView(LoginRequiredMixin, UpdateView):
#     model = CustomUser
#     form_class = ProfileUpdateForm
#     template_name = "auth_system/profile_edit.html"
#     success_url = reverse_lazy("profile")

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

#     def get_object(self):
#         return self.request.user

# class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = CustomUser
#     template_name = "auth_system/admin_user_list.html"
#     context_object_name = "users"

#     def test_func(self):
#         return self.request.user.is_superuser or self.request.user.groups.filter(name="admin").exists()

# class UserRoleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = CustomUser
#     form_class = UserRoleForm
#     template_name = "auth_system/admin_user_edit.html"
#     success_url = reverse_lazy("admin-users-list")

#     def test_func(self):
#         return self.request.user.is_superuser or self.request.user.groups.filter(name="admin").exists()