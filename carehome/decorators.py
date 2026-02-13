from django.shortcuts import redirect
from functools import wraps


def role_based_access(allowed_roles=[]):
    """
    Restrict access to views based on user role.
    Example:
        @role_based_access(['manager', 'senior_carer', 'carer'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if (request.user.is_authenticated and
                    request.user.role in allowed_roles):
                return view_func(request, *args, **kwargs)
            return redirect('/')  # Unauthorized users go to home
        return wrapper
    return decorator