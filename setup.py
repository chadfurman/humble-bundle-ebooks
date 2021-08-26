# Import needed function from setuptools
from setuptools import setup, find_packages

# Create proper setup to be used by pip
setup(name='humble-bundle-api',
      version='0.0.1',
      description='Python interface to humble bundle library',
      author='Lotus',
      packages=find_packages(include=['pytest']),
      install_requires=[
          "pytest",
          "colorama",
          "sqlalchemy",
          "graphene>=2.0",
          "sqlitedict"])

