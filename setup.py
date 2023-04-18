from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='sphinx_favicon',
   version='1.0.1',
   description='Add custom favicons to your Sphinx html documentation quickly and easily.',
   license="MIT",
   long_description=long_description,
   author='Timo Cornelius Metzger',
   author_email='coding@tcmetzger.net',
   url="https://github.com/tcmetzger/sphinx-favicon",
   packages=['sphinx_favicon'],
   install_requires=[],
   scripts=[]
)
