from core.cms.views import HomeView, LoginViewCustom, LogoutViewCustom, UserListView, UserCreateView
from django.urls import path

app_name = 'cms'

urlpatterns = [
    path('login', LoginViewCustom.as_view(), name='login'),
    path('logout', LogoutViewCustom.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('user', UserListView.as_view(), name='user'),
    path('user/create', UserCreateView.as_view(), name='user-create'),
]