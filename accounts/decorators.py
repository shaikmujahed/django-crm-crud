from django.http import HttpResponse
from django.shortcuts import redirect


def unauthorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.all()[0].name == 'customer':
            return redirect('products')
        else:
            return view_func(request, *args, **kwargs)

        if request.user.groups.all()[0].name == 'admin':
            return redirect('index')

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to access this')

        return wrapper_func

    return decorators