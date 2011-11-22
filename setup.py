from setuptools import setup

setup(
    name='django-celery-xa',
    version=__import__('celery_xa').__version__,
    description='Attempt to execute celery tasks after transaction commit!',
    author='German Ilyin',
    author_email='germanilyin@gmail.com',
    url='https://github.com/yunmanger1/django-celery-xa/',
    packages=['celery_xa','celery_xa.utils',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

