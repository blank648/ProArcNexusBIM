import threading
from django.utils.deprecation import MiddlewareMixin

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class AuditMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _thread_locals.user = request.user if request.user.is_authenticated else None

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Pentru post_save signal:
        from django.db.models import Model
        def _set_user(instance, **kwargs):
            if isinstance(instance, Model):
                setattr(instance, '_current_user', _thread_locals.user)