from setuptools import setup
import setuptools

with open('README.MD', 'r') as f:
    long_description = f.read()

setup(
    name='instapy',
    version='0.1.0',
    author='Kun Zhu',
    author_email='kunzh@uio.no',
    packages=setuptools.find_packages(),
    scripts=['bin/instapy'],
    url='https://github.uio.no/IN3110/IN3110-kunzh/tree/master/assignment4/instapy',
    # license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=['numpy', 'numba', 'opencv_python', 'pytest'],
)