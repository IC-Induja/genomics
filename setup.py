from setuptools import find_packages, setup

long_description = '''
TODO: put description of our library here
'''

setup(name='genomics',
      version='0.0.1',
      description='TODO: write short description',
      long_description=long_description,
      author='Induja Chandrakumar',
      author_email='ic.induja@gmail.com',
      url='https://github.com/IC-Induja/genomics',
      license='MIT',
      install_requires=['pandas>=0.23.4',
                        'six>=1.11.0'],
      extras_require={
          'tests': ['pytest'],
      },
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Healthcare Industry',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Bio-Informatics'
      ],
      packages=find_packages())
