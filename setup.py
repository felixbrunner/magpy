from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="beewits",
    version="0.1",
    description="Program to create html website from markdown files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="felixbrunner",
    author_email="",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
