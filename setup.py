from setuptools import setup, find_packages
import pathlib


setup (
    name = "JobFunClassifier",
    version = "0.7.1",
    description="The JobFunClassifier is a Python package designed for NLP-based job function classification.",
    long_description= pathlib.Path("README.md").read_text(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/LULUCHIU/JobFunClassifier.git",
    author = "LuTing(Tina) Chiu",
    author_email="tinachiu.tech@gmail.com",
    license="The Unlicense",
    project_urls = {
        "Source":"https://github.com/LULUCHIU/JobFunClassifier.git"
    },
    classifiers= [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing",
        "Topic :: Utilities"
    ],
    python_requires = ">= 3.10, <3.12",
    packages = find_packages(),
    install_requires = ["nltk>=3.8","numpy>=1.25","pandas>=2.0","scipy>=1.5.0","threadpoolctl>=2.0.0","scikit-learn>=1.3"],
    include_package_data=True,
    entry_points = {"console_scripts": ["JobFunClassifier = JobFunClassifier.model:JobFunClassifier"]}
)