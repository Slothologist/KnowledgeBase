from setuptools import setup, find_packages

setup(name='knowledge_base',
      version='0.1.0',
      description='Simple ros database for the robocup at home league.',
      url='---none---',
      author='rfeldhans',
      author_email='rfeldhans@techfak.uni-bielefeld.de',
      license='---none---',
      packages=find_packages(),
      install_requires=[
          'pymongo',
          'mongoengine'
      ])