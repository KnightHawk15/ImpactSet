# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='ImpactSet',
    version='1.0.0',
    description='Package to identify a foods environmental impact',
    url='https://github.com/KnightHawk15/ImpactSet.git',
    author='Ethan Peters',
    author_email='espeters10@gmail.com',
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
)