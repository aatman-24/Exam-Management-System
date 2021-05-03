from django.contrib.auth.decorators import  login_required, permission_required, user_passes_test, wraps
from django.utils.decorators import method_decorator
from django.views.generic import  View
from django.core.exceptions import ImproperlyConfigured

def custom_login_required(view): #view must be a method
    decorator = method_decorator(login_required)
    decorated_view = decorator(view)
    return decorated_view

def class_login_required(cls):  #directly can apply to the class

    if(not isinstance(cls, type) or not issubclass(cls, View)):
        raise ImproperlyConfigured("class_login_required\nMust be applied to subclasses of View Class.")
    
    decorator = method_decorator(login_required)
    cls.dispatch = decorator(cls.dispatch)
    return cls

def require_authenticated_permisssion(permission):

    def decorator(view): #view must be a function
        check_auth = login_required
        check_perm = permission_required(permission, raise_exception=True)

        decorated_view = check_auth(check_perm(view))
        return decorated_view
    
    return decorator

def class_require_authenticated_permisssion(permission):    #directly can apply to the class

    def decorator(cls):
        if(not isinstance(cls, type) or not issubclass(cls, View)):
            raise ImproperlyConfigured("class_login_required\nMust be applied to subclasses of View Class.")
        check_auth = method_decorator(login_required)
        check_perm = method_decorator(permission_required(permission, raise_exception=True))
        cls.dispatch = check_auth(check_perm(cls.dispatch))
        return cls
        
    return decorator

