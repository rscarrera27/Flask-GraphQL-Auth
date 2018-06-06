from setuptools import setup

setup(
    name='Flask-GraphQL-Auth',
    version=0.1,
    url="https://github.com/devArtoria/flask-graphql-auth",
    license='MIT',
    author='Lewis "devArtoria" Kim',
    author_email='artoria@artoria.us',
    description="JWT library for flask-graphql",
    packages=['flask_graphql_auth'],
    requires=[
        'Flask',
        'pyjwt'
    ]
)