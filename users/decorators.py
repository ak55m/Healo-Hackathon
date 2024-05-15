from django.http import HttpResponseForbidden

def non_doctor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_doctor:
            return HttpResponseForbidden("This area is restricted to non-doctors.")
        return view_func(request, *args, **kwargs)
    return wrapper
