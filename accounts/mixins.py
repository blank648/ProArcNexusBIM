from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.models import Utilizator
from typing import cast

#atribuit allowed_roles
class RoleRequiredMixin(UserPassesTestMixin):
    request: HttpRequest
    allowed_roles = []
    login_url = reverse_lazy('accounts:login')
    permission_denied_message = 'Actiune interzisa'

    #verifica self.request.user.is_authenticated si user.role in allowed_roles
    def test_func(self):
        user = cast(Utilizator, self.request.user)
        return user.is_authenticated and user.role in self.allowed_roles

    #redirectioneaza login neadecvat
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return self.handle_no_permission()
        return redirect('permission_denied')