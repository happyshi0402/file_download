'''
file_download
-----------

file_download provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

file_download is not bound to any particular database system or permissions
model. The only requirement is that your user objects implement a few
methods, and that you provide a callback to the extension capable of
loading users from their ID.

Links
`````
* `documentation <http://packages.python.org/file_download>`_
* `development version <https://github.com/maxcountryman/file_download>`_
'''
import os
import sys

from setuptools import setup

about = {}
with open('file_download/__about__.py') as f:
    exec(f.read(), about)

if sys.argv[-1] == 'test':
    status = os.system('make check')
    status >>= 8
    sys.exit(status)

setup(name=about['__title__'],
      version=about['__version__'],
      url=about['__url__'],
      license=about['__license__'],
      author=about['__author__'],
      author_email=about['__author_email__'],
      description=about['__description__'],
      long_description=__doc__,
      py_modules=['file_download'],
      zip_safe=False,
      platforms='any',
      install_requires=[''],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ])
