from setuptools import setup, find_packages

setup(
    name='numbertheory',
    version='0.1',
    description='Common number theoretic functions.',
    packages=find_packages(where='number-theory'),
    package_dir={'': 'number-theory'},
    license='GPL-3.0 license',
    url='https://0xkilty.github.io/number-theory/',
    author='0xKilty',
    author_email='ian.kilty@colostate.edu',
    install_requires=[
        
    ],
)