from django.shortcuts import redirect
from functools import wraps


def role_required(allowed_roles):
    """
    Only allow users whose role is in allowed_roles.
    Redirect others to home.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('account_login')  # redirect if not logged in
            if request.user.role not in allowed_roles:
                return redirect('home')  # or render 403 page
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

