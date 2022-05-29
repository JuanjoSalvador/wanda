
from setuptools import setup, find_packages
from os import path

currdir = path.abspath(path.dirname(__file__))
with open(path.join(currdir, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(name='wandaengine',
      version='0.0.1',
      install_requires=["PySDL2"],
      url='https://github.com/juanjosalvador/wanda',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      license='MIT',
      author='Juanjo Salvador',
      author_email='juanjosalvador@netc.eu',
      packages=find_packages(exclude=['sample']),
      zip_safe=False)