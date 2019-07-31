from setuptools import setup

setup(
    name='Flask-MSSQL',
    version='1.0',
    url='http://example.com/flask-mssql/',
    license='BSD',
    author='Christopher Thompson',
    author_email='csthompson521@gmail.com',
    description='Connects to MSSQL'
    long_description=__doc__,
    py_modules=['flask_mssql'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ]
    classifiers=[
        'Environment' :: Web Environment',
        'Intended Audience' :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)