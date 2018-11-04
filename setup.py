# -*- coding: UTF-8 -*-


try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


requires = ['requests', 'lxml']

packages = ['siteranklib']


setup(
	name='siteranklib',
	version='0.1.3',
	description='Python lib that provides you with some usefull and simple methods to obtain website metrics',
	long_description=open('README.rst').read(),
	author='Duc Bui',
	author_email='ducbuihoang@gmail.com',
	license=open('LICENSE').read(),
	url='https://github.com/ducalpha/siteranklib',

	include_package_data=True,
	packages=packages,
	install_requires=requires,

	classifiers=(
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'License :: OSI Approved :: Apache Software License',
		'Intended Audience :: Developers',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python',
	    'Programming Language :: Python :: 3.6',
	),
)
