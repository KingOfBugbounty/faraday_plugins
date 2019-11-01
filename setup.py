from setuptools import setup, find_packages
from re import search

with open('faraday_plugins/__init__.py', 'rt', encoding='utf8') as f:
    version = search(r'__version__ = \'(.*?)\'', f.read()).group(1)


install_requires = [
    'Click',
    'simplejson',
    'requests',
]


setup(
    name='faraday-plugins',
    version=version,
    packages=find_packages(include=['faraday_plugins', 'faraday_plugins.*']),
    url='',
    license='',
    author='Faradaysec',
    author_email='',
    description='',
    include_package_data=True,
    install_requires=install_requires,
)