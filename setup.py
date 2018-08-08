from setuptools import setup

requirements = open('requirements.txt', 'r').read().split("\n")

setup(
    name='nif',
    version='profit-v16',
    packages=['nif'],
    license='MIT',
    install_requires=requirements,
    description="NLP interchange format library for Python"
)
