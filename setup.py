from setuptools import setup, find_packages, dist

build_requires = [package for package,version in
                  [line.split ("==") for line in
                   open("requirements.txt").read().split("\n") if line]]

setup(
    name="{{cookiecutter.service_name}}",
    version="1.0.1",
    #url="http://",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",,
    packages=find_packages(),
    #setup_requires = build_requires,
    #install_requires = build_requires,
)
