
from setuptools import setup, find_packages

setup(
    name="TiktokResearchApi",
    version="1.0.0",
    description="A Python package for interacting with the TikTok Research API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="",
    url="",
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "requests>=2.20.0",
    ],
    python_requires=">=3.6",
)