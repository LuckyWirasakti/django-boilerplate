from django.db.models import fields
import django_tables2 as tables
from django.contrib.auth.models import User

class UserTable(tables.Table):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined'
        )
