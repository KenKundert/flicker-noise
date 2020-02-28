# This file is used to install the dependencies for runPnoise and runBSIM.
# You can get the dependencies using either of the following commands:
#     pip3 install --user .
# or:
#     python3 setup.py install --user

from setuptools import setup

dependencies = """
    docopt
    matplotlib
    numpy
    inform
    quantiphy>=2.9
    psf-utils>=0.3
    shlib
    svg_schematic
"""

setup(
    name="flicker-noise",
    description="runs flicker noise simulations",
    author="Geoffrey Coram, Colin McAndrew, Kiran Gullapalli and Ken Kundert",
    author_email="ken@designers-guide.com",
    version="1.0.1",
    license="GPLv3+",
    # script='runPnoise runBSIM'.split(),
    install_requires=dependencies.split(),
    python_requires=">=3.6",
)
