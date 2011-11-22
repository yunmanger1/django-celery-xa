from django.db import transaction
from django.dispatch.dispatcher import receiver
from .queue import store
import logging
log = logging.getLogger('DEFAULT')

@receiver(transaction.signals.post_commit) #@UndefinedVariable
def after_commit(*args, **kwargs):
    
    for obj in store.queue:
        if callable(obj):
            obj()
            print obj
            log.debug('asdasd')
    store.clear()
    if transaction.is_dirty():
        transaction.commit()
    