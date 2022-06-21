from setuptools import setup

setup(
 name='mypackage',
 version='1.0.0',
 author='Danila Solodennikov',
 packages=['mypackage', 'mypackage.test'],
 scripts=['main.py','Tests.py','solution.py'],
 url='https://github.com/Master-sniffer/testing-with-python/mypackage',
 description='Test task',
 long_description=open('README.md').read(),
 install_requires=[
     "pycodestyle",
     "flake8",
     "pytest",
 ],
)