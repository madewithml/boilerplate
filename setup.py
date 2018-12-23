from setuptools import setup, find_packages, dist

build_requires = [package for package,version in
                  [line.split ("==") for line in
                   open("requirements.txt").read().split("\n") if line]]

setup(
    name="document_classification",
    version="1.0.1",
    description="document classification",
    #url="http://",
    author="Goku Mohandas",
    author_email="gokumd@gmail.com",
    long_description="Document classification",
    packages=find_packages(),
    #setup_requires = build_requires,
    #install_requires = build_requires,
)
