from setuptools import setup, find_packages

setup(
  name = 'japanese-numbers-python',
  version = '0.2.1',
  packages = find_packages(
    '.',
    exclude = [
      '*.tests', '*.tests.*', 'tests.*', 'tests',
    ]
  ),
  package_dir = {
    '' : '.'
  },
  author = 'Takumakanari',
  author_email = 'chemtrails.t@gmail.com',
  maintainer = 'Takumakanari',
  maintainer_email = 'chemtrails.t@gmail.com',
  description = 'A parser for Japanese number (Kanji, arabic) in the natulal language.',
  classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  install_requires = ['future>=0.16.0', 'nose'],
  license = 'MIT',
  keywords = 'japanese numbers parser kanji arabic',
  zip_safe = True,
  include_package_data = True
)

