# -*- coding: utf-8 -*8-

from setuptools import setup, find_packages

from todomvc import version


setup(
    name='django-todomvc',
    version=version.to_str(),
    description='TodoMVC django app',
    author='Adones Cunha',
    author_email='adonescunha@gmail.com',
    url='https://github.com/adonescunha/django-todomvc',
    packages=find_packages(exclude=['tests']),
    package_data={
        'todomvc': [
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
    install_requires=[
    ],
    zip_safe=False,
)
