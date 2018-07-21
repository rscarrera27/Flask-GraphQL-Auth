from setuptools import setup

setup(
    name='Flask-GraphQL-Auth',
    version=0.3,
    url="https://github.com/devArtoria/flask-graphql-auth",
    license='MIT',
    author='Lewis "devArtoria" Kim',
    author_email='artoria@artoria.us',
    keywords=['jwt', 'auth', 'graphql'],
    description="JWT library for Flask-GraphQL",
    packages=['flask_graphql_auth'],
    requires=[
        'Flask',
        'pyjwt',
        'Flask_graphql'
    ]
)