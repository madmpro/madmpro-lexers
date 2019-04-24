#!/usr/bin/env python
"""Setup madmpro-lexers."""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
bsl=madmpro_lexers.bsl:Lang1CLexer
'''

setup(
    name='madmpro-lexers',
    version='1.0.0',
    description='Pygments lexer package for Pygments.',
    author='madm.pro',
    author_email='madm[dot]pro [at] gmail.com',
    url='https://github.com/madmpro/madmpro-lexers',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
