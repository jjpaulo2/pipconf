import setuptools

from pipconf import __version__
from pipconf import __description__
from pipconf import __name__
from pipconf import __index__

from pipconf import __author__
from pipconf import __author_email__


with open("readme.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name=__name__, 
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__index__,
    project_urls={
        "Bug Tracker": __index__ + "/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux :: Mac OS",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
