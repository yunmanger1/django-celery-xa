Attempt to execute celery tasks after transaction commit!

Based on https://gist.github.com/247844 by Grégoire Cachet

~~~~
from celery.task import task
from celery_xa.utils.patcher import celery_xa_patch

@celery_xa_patch
@task
def add(x, y):
    return x + y
    
    
# if settings.BROKER_TRANSPORT == "django" or transaction.is_managed() == False task will be executed normally,
# otherwise it will be executed after commit.  
add.delay(2,3)
~~~~

