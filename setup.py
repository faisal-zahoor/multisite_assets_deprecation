from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in test/__init__.py
from test import __version__ as version

setup(
	name="test",
	version=version,
	description="For testing purpose only",
	author="Havenir Solutions",
	author_email="havenirnomi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
