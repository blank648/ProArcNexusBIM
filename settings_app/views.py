from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import SetareGenerala
from .forms import SetareGeneralaForm
from accounts.mixins import RoleRequiredMixin

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'admin'

class SetareListView(RoleRequiredMixin, AdminRequiredMixin, ListView):
    allowed_roles = ['admin']
    model = SetareGenerala
    template_name = 'settings_app/setare_list.html'
    paginate_by = 20

class SetareCreateView(RoleRequiredMixin, AdminRequiredMixin, CreateView):
    allowed_roles = ['admin']
    model = SetareGenerala
    form_class = SetareGeneralaForm
    template_name = 'settings_app/setare_form.html'
    success_url = reverse_lazy('settings_app:list')

class SetareUpdateView(RoleRequiredMixin, AdminRequiredMixin, UpdateView):
    allowed_roles = ['admin']
    model = SetareGenerala
    form_class = SetareGeneralaForm
    template_name = 'settings_app/setare_form.html'
    success_url = reverse_lazy('settings_app:list')

class SetareDeleteView(RoleRequiredMixin, AdminRequiredMixin, DeleteView):
    allowed_roles = ['admin']
    model = SetareGenerala
    template_name = 'settings_app/setare_confirm_delete.html'
    success_url = reverse_lazy('settings_app:list')