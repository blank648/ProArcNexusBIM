from django.views.generic import ListView
from .models import ChangeLog
from django.contrib.auth.mixins import UserPassesTestMixin
from accounts.models import Utilizator

#afiseaza ChangeLog paginat
class AuditLogView(UserPassesTestMixin ,ListView):
    allowed_roles = ['admin', 'manager']
    model = ChangeLog
    template_name = 'audit/changelog_list.html'
    paginate_by = 50
    login_url = 'accounts:login'

    def test_func(self):
        if not isinstance(self.request.user, Utilizator):
            return False
        return self.request.user.is_authenticated and self.request.user.role in self.allowed_roles
