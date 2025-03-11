from setuptools import find_packages, setup

from ._version import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aloha_api",
    version=__version__,
    author="Jordan Haisley",
    author_email="jordanhaisley@gmail.com",
    description="A Python client for the Aloha ABA Practice Management Software API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhaisley/aloha_api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "python-dotenv>=0.19.0",
        "tomli>=2.0.0",
    ],
)
