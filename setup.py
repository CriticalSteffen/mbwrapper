"""Malware Bazaar API Wrapper Setup File."""

import pathlib
import re

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
PACKAGE_NAME = "mbwrapper"

CONST_TEXT = (HERE / f"{PACKAGE_NAME}/const.py").read_text()
VERSION = re.search('__version__ = "([^\']+)"', CONST_TEXT).group(1)

setup(
    name="MBWrapper",
    version=VERSION,
    description="A Python3 wrapper for the MalwareBazaar API.",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="malware bazaar api library",
    url="https://github.com/CriticalSteffen/mbwrapper",
    project_urls={
        "Source Code": "https://github.com/CriticalSteffen/mbwrapper",
        "Documentation": "https://github.com/CriticalSteffen/mbwrapper",
    },
    author="Christopher Steffen",
    author_email="christopher.steffen@criticalstart.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=[PACKAGE_NAME],
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    entry_points={},
)
