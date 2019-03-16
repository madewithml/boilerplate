from setuptools import setup, find_packages

requirements = [package for package in open("requirements.txt").read().split("\n") if package]

setup(
    name="{{ cookiecutter.package_name }}",
    version="0.0.1",
    description="{{ cookiecutter.service_name }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.service_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    packages=find_packages(),
    setup_requires=["Flask==1.0.2"],
    install_requires=requirements,
    python_requires=">=3.6",
    test_suite="tests",
)