#! /usr/bin/env python
#
# Copyright (C) 2014-2017 Mikko Kotila

import os
os.environ["MPLCONFIGDIR"] = "."

DESCRIPTION = "Autonomio deep learning workbench "
LONG_DESCRIPTION = """\
Autonomio provides a very high-level abstraction layer on top of Keras,
using Tensorflow as a backend and spaCy for word vectorization.

- single-command neural network training
- training command accepts as little as 'x' and 'y' as inputs
- 'x' can be text, continues or categorial data
- 15 optional configurations from a single command
- seamlessly integrates word2vec with keras deep learning
- interactive plots specifically designed for deep learning

For most use cases succesfully running a state-of-the-art AI works
out of the box in less than 60 seconds to first trained model.

"""

DISTNAME = 'autonomio'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://autonom.io'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/autonomio/core-module/'
VERSION = '0.4'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():

    install_requires = []

    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')
    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')
    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')
    try:
        import tensorflow
    except ImportError:
        install_requires.append('tensorflow')
    try:
        import keras
    except ImportError:
        install_requires.append('keras')
    try:
        import spacy
    except ImportError:
        install_requires.append('spacy')
    try:
        import h5py
    except ImportError:
        install_requires.append('h5py')
    try:
        import mpld3
    except ImportError:
        install_requires.append('mpld3')
    try:
        import jinja2
    except ImportError:
        install_requires.append('jinja2')
    try:
        import iPython
    except ImportError:
        install_requires.append('iPython')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=install_requires,
        packages=['autonomio',
                  'autonomio.plots',
                  'autonomio.transform',
                  'autonomio.utils',
                  'autonomio.models'],

        classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                     'Topic :: Scientific/Engineering :: Artificial Intelligence',
                     'Topic :: Scientific/Engineering :: Mathematics',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
)

os.system("python -m spacy download en")
