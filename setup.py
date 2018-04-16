# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:10:53 2018

@author: Peng
"""

from setuptools import setup

setup(
      name = 'shipy',
      version = '0.01',
      description = 'Multivariant Shannon Information',
      author = 'Pengwyn',
      author_email = '@',
      url = 'https://github.com/ThePengwyn/shipy',
      download_url = 'https://github.com/ThePengwyn/shipy/archive/0.01.tar.gz'
      packages = ['shipy'],
      install_requires = [
              'numpy',
              'scipy'
              ]
      )
