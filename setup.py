from setuptools import find_packages, setup

setup(
    name="linux-notes-cli",
    version="1.0.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["lnotes=lnotes.main:main"]},
)
