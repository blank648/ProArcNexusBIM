# File: ProArcNexus2/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'total_clients': request.user.has_perm('clients.view_client') and
                         __import__('clients.models').clients.models.Client.objects.count() or None,
        'total_articles': request.user.has_perm('articles.view_articol') and
                          __import__('articles.models').articles.models.Articol.objects.count() or None,

    }
    return render(request, 'dashboard.html', context)

def home_base(request):
    return render(request, 'base.html')
