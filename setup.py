from setuptools import find_packages
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    name='knowledge_base',
    version='0.1.0',
    description='Simple ros database for the robocup at home league.',
    url='---none---',
    author='rfeldhans',
    author_email='rfeldhans@techfak.uni-bielefeld.de',
    license='---none---',
    install_requires=[
        'xml.dom',
        'xml.etree',
        'pymongo',
        'mongoengine'
      ],
    packages=find_packages())

setup(**setup_args)