from distutils.core import setup
from setuptools import find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'statistical_iv',       
  packages = find_packages(), 
  version = '0.3.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Statistical IV: Statistical Hypothesis Testing for the Information Value (IV). Evaluation of the predictive power of features using the IV with specific thresholds for each dataset.', #'Statistical IV: J-Divergence Hypothesis Test for the Information Value (IV)', # An statistical use of information value with a defined predictived power',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = ' Nilton Rojas, Helder Rojas',
  maintainer="Nilton Rojas Vales",
  maintainer_email="nrojasv@uni.pe",
  url = 'https://github.com/Nicerova7/statistical_iv',   # Provide either the link to your github or to your website
  keywords = ['information_value', 'woe', 'data science', 'hypothesis test'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
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