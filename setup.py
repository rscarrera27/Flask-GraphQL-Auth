from setuptools import setup

setup(
    name='Flask-GraphQL-Auth',
    version='1.1.1',
    url="https://github.com/devArtoria/flask-graphql-auth",
    license='MIT',
    author='devArtoria',
    author_email='artoria@artoria.us',
    keywords=['jwt', 'auth', 'graphql'],
    description="JWT library for Flask-GraphQL",
    packages=['flask_graphql_auth'],
    install_requires=[
        'PyJWT',
        'Flask_GraphQL',
        'graphene'
    ]
)