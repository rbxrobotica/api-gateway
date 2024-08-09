from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model

class BalanceCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            cost = getattr(view_func, 'cost', 0)
            if request.user.balance < cost:
                return JsonResponse({"error": "Saldo insuficiente."}, status=402)
        return None
