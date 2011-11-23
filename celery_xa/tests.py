# coding: utf-8
from django.test import TestCase
from django.db import transaction
from django.contrib.auth.models import User
from celery.task import task

class SimpleTest(TestCase):

    @transaction.commit_on_success
    def test_0001(self):
        # надо для падчинга
        from celery_xa.patcher import celery_xa_patch

        @celery_xa_patch
        @task
        def add(a, b):
            return a + b

        self.assertEqual(transaction.is_dirty(), False)
        user = User(username = 'test_0001')
        user.save()
        self.assertEqual(transaction.is_dirty(), True)
        add.delay(2, 3)

