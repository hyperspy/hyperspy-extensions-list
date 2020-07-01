from setuptools import setup

with open('extension_list.txt') as fp:
    install_requires = fp.read()

setup(name='hyperspy-extensions-list',
      install_requires=install_requires,
     )

