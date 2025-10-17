from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import Client
from .forms import ClientForm
from django.db.models import Q
from accounts.mixins import RoleRequiredMixin

#views mostenesc RequiredMixin cu roluri permise
#afiseaza object_list paginate
class ClientListView(RoleRequiredMixin, ListView):
    #roluri permise
    allowed_roles = ['admin','manager','user']
    model = Client
    template_name = 'clients/client_list.html'
    paginate_by = 20

    def get_queryset(self):
        q = self.request.GET.get('q','')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(cui__icontains=q)
            )
        return qs

#formular de creare client, redirect la lista
class ClientCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ['admin','manager']
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients::list')

#editare client existent
class ClientUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['admin','manager']
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients::list')

#confirmare si stergere client
class ClientDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = ['admin']
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('clients::list')
