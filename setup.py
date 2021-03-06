# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='alpg',
      version='1.0.dev0',
      description='ArchLinux Package Generator',
      long_description=readme(),
      url='',
      author='Benoît Zugmeyer',
      author_email='bzugmeyer@gmail.com',
      license='Expat',
      packages=['alpg'],
      install_requires=[
          'Click>=6,<7',
      ],
      entry_points={
          'console_scripts': ['alpg=alpg.__init__:cli'],
      },
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=True)
