from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'statistical_iv',       
  packages = find_packages(), 
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Statistical_IV: J-Divergence Hypothesis Test for the Information Value (IV)', # An statistical use of information value with a defined predictived power',   # Give a short description about your library
  author = ' Nilton Rojas, Helder Rojas, Cirilo Alvarez',
  maintainer="Nilton Rojas Vales",
  maintainer_email="nrojasv@uni.pe",
  url = 'https://github.com/Nicerova7/statistical_iv',   # Provide either the link to your github or to your website
  keywords = ['information_value', 'woe', 'data science', 'hypothesis test'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy'
          'scipy',
          'optbinning'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Information Technology',      # Define that your audience are developers
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)