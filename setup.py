# This file is used to install the dependencies for runPnoise and runBSIM.
# You can get the dependencies using either of the following commands:
#     pip3 install --user .
# or:
#     python3 setup.py install --user

from setuptools import setup

dependencies = 'docopt matplotlib numpy inform quantiphy psf-utils>=0.3 shlib'

setup(
    name='flicker-noise',
    description='runs flicker noise simulations',
    author="Colin McAndrew, Geoffrey Coram and Ken Kundert",
    author_email='ken@designers-guide.com',
    license='GPLv3+',
    #script='runPnoise runBSIM'.split(),
    install_requires=dependencies.split(),
    python_requires='>=3.6',
)
