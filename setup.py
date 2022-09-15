from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in equipment/__init__.py
from equipment import __version__ as version

setup(
	name="equipment",
	version=version,
	description="This app made for equipment.com",
	author="Nilesh Pithiya",
	author_email="nilesh.pithiya@sanskartechnolab.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
