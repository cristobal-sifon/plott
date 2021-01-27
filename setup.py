from __future__ import (absolute_import, division, print_function)


import os
import re
from setuptools import find_packages, setup

# folder where pygmos is stored
here = os.path.abspath(os.path.dirname(__file__))

#this function copied from pip's setup.py
#https://github.com/pypa/pip/blob/1.5.6/setup.py
#so that the version is only set in the __init__.py and then read here
#to be consistent
def find_version(fname):
    version_file = read(fname)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


#Taken from the Python docs:
#Utility function to read the README file.
#Used for the long_description.  It's nice, because now 1) we have a
#top level README file and 2) it's easier to type in the README file
#than to put a raw string in below
def read(fname):
    return open(os.path.join(here, fname)).read()




setup(
    name='plott',
    version=find_version('plott/__init__.py'),
    description='Custom plotting tools',
    author='Cristobal Sifon',
    author_email='cristobal.sifon@pucv.cl',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/cristobal-sifon/plott',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Visualization',
        ],
)
