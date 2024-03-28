from setuptools import setup, find_packages

with open('../README.md', 'r') as readme:
    long_descripton = readme.read()
    
setup(
    name='numbertheory',
    version='0.0.2',
    description='Common number theoretic functions.',
    long_description_content_type='text/markdown',
    long_description=long_descripton,
    packages=find_packages(),
    license='MIT',
    url='https://0xkilty.github.io/number-theory/',
    author='0xKilty',
    author_email='ian.kilty@colostate.edu',
    extras_require={
        'dev': ['twine>=4.0.2']
    },
    classifiers=[
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)