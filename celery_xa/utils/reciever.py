from django.db import transaction
from django.dispatch.dispatcher import receiver
from .queue import store
import logging
log = logging.getLogger('DEFAULT')

@receiver(transaction.signals.post_commit) #@UndefinedVariable
def after_commit(*args, **kwargs):
#    log.debug('commit')
    for obj in store.queue:
        if callable(obj):
            obj()
    store.clear()
    if transaction.is_dirty():
        transaction.commit()
