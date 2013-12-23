import setuptools
import sys

tests_require = ['nose', 'mock']
if sys.version_info < (2, 7, 0):
    tests_require.append('unittest2')

desc = ('A pure python, thread-safe, minimalistic and pythonic RabbitMQ '
        'client library')

setuptools.setup(name='rabbitpy',
                 version='0.12.2',
                 description=desc,
                 long_description=open('README.rst').read(),
                 author='Gavin M. Roy',
                 author_email='gavinmroy@gmail.com',
                 url='http://rabbitpy.readthedocs.org',
                 packages=['rabbitpy'],
                 package_data={'': ['LICENSE', 'README.md']},
                 include_package_data=True,
                 install_requires=['pamqp>=1.2.0'],
                 tests_require=tests_require,
                 test_suite='nose.collector',
                 license=open('LICENSE').read(),
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: BSD License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python :: 2',
                              'Programming Language :: Python :: 2.6',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3',
                              'Programming Language :: Python :: 3.2',
                              'Programming Language :: Python :: 3.3',
                              'Programming Language :: Python :: Implementation :: CPython',
                              'Programming Language :: Python :: Implementation :: PyPy',
                              'Topic :: Communications',
                              'Topic :: Internet',
                              'Topic :: Software Development :: Libraries'],
                 zip_safe=True)
