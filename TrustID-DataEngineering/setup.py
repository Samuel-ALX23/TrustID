from setuptools import setup, find_packages

setup(
    name="trustid",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "redis",
        "cryptography",
        "indy"
    ]
)
