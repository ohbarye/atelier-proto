from setuptools import setup, find_packages

setup(
    name='atelier',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        'gunicorn',
        'whitenoise',
        'dj_database_url',
    ],
)
