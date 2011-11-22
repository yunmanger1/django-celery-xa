#coding: utf-8
from django.conf import settings
from .utils.queue import store
from django.utils.functional import curry
from django.db import transaction

def wrap_func(func):
    old_func = func
    def new_func(*args, **kwargs):        
        if settings.BROKER_TRANSPORT == "django" or not transaction.is_managed():
            # если используется db транспорт или мы не под транзакцией, то нам это не нужно.
            # все работает по старому 
            return old_func(*args, **kwargs)
        else:
            store.queue.append(curry(old_func, *args, **kwargs)) #@UndefinedVariable
    return new_func
    

def celery_xa_patch(func):
    """
    Патчаем delay и apply_async
    """
    func.apply_async = wrap_func(func.apply_async) 
    func.delay = wrap_func(func.delay) 
    return func