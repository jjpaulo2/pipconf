import setuptools

from pipconf import __version__
from pipconf import __description__
from pipconf import __module__
from pipconf import __index__
from pipconf import __license__

from pipconf import __author__
from pipconf import __author_email__


with open("readme.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name=__module__, 
    version=__version__,
    description=__description__,
    license=__license__,

    long_description=long_description,
    long_description_content_type="text/markdown",

    author=__author__,
    author_email=__author_email__,

    url=__index__,
    project_urls={
        "Bug Tracker": __index__ + "/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3"
    ],

    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points = {
        'console_scripts': ['pipconf=pipconf.cli:main'],
    },
    
    python_requires=">=3.6",
)
