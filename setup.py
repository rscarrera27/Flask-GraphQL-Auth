from setuptools import setup, find_packages

setup(
    name='auge',
    version=0.1,
    url="https://github.com/devArtoria/Auge",
    license='MIT',
    author='Lewis Kim',
    author_email='artoria@artoria.us',
    description="a simple JWT library",
    packages=find_packages(),
    requires=[
        'pyjwt'
    ]
)