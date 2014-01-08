from setuptools import setup


setup(
    name='flask-headers',
    version='1.0',
    url='https://github.com/wcdolphin/flask-headers',
    license='MIT',
    author='Cory Dolphin',
    author_email='wcdolphin@gmail.com',
    description="A Flask extension making awesome headers one decorator away",
    long_description=__doc__,
    py_modules=['flask_headers'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)