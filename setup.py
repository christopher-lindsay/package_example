from setuptools import find_packages, setup

setup(
	name="my_package",
	packages=find_packages(where="my_package"),
	package_dir={"": "."}
)

