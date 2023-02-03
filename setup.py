"""
grow
-----------

grep by codeowners
"""
from os import path

import versioneer
from setuptools import setup, find_packages

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, "README.md"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()
with open(path.join(this_dir, "requirements/production.txt"), encoding="utf-8") as requirements_file:
    requirements = requirements_file.read().splitlines()


setup(
    name="grow",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="grep by codeowners",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abenezer Mamo",
    author_email="hi@abenezer.sh",
    license="MIT",
    packages=find_packages(exclude=("tests", "venv")),
    install_requires=requirements,
    zip_safe=False,
    entry_points = {
        "console_scripts": ["grow=src.__main__:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)