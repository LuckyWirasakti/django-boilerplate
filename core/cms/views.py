from core.cms.forms import AuthenticationFormCustom
from core.cms.mixins import SingleSearchTableView
from core.cms.tables import UserTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class LoginViewCustom(LoginView):
    form_class = AuthenticationFormCustom
    template_name = 'cms/auth/base.html'
    redirect_authenticated_user = True


class LogoutViewCustom(LogoutView):
    pass


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'cms/home.html'
    extra_context = {
        'page_title': 'Home',
        'page_pretitle': 'Welcome back to home',
    }


class UserListView(LoginRequiredMixin, SingleSearchTableView):
    model = User
    table_class = UserTable
    template_name = 'cms/user/list.html'
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    extra_context = {
        'page_title': 'User',
        'page_pretitle': 'Select user to change',
        'href': 'cms:user-create',
    }


class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'cms/user/form.html'
    extra_context = {
        'page_title': 'User',
        'page_pretitle': 'Select user to change',
    }
