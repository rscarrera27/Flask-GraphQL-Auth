import os
import re

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open(os.path.join("flask_graphql_auth", "__init__.py"), "r") as f:
    try:
        version = re.findall(r"^__version__ = \"([^']+)\"\r?$", f.read(), re.M)[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")

install_requires = [
    "flask",
    "graphene",
    "PyJWT==2.4.0"
]

tests_requires = [
    "pytest==4.4.2",
    "pytest-cov==2.7.1",
    "coverage==4.5.3",
    "pytest",
    "graphql_server==3.0.0b5"
]

dev_requires = [] + tests_requires


setup(
    name="Flask-GraphQL-Auth",
    version=version,
    url="https://github.com/NovemberOscar/Flask-GraphQL-Auth",
    license="MIT",
    author="NovemberOscar",
    author_email="kim@seonghyeon.dev",
    keywords=["jwt", "auth", "graphql"],
    description="JWT library for Flask-GraphQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["flask_graphql_auth"],
    install_requires=install_requires,
    tests_requires=tests_requires,
    extras_require={
        'test': tests_requires,
        'dev': dev_requires,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
