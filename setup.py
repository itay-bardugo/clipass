import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

#packaging
setuptools.setup(
    name="clipass",
    version="0.0.0",
    author="Itay Bardugo",
    author_email="itaybardugo91@gmail.com",
    description="CLI passowrd generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itay-bardugo/clipass",
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "clipass = clipass.main:main"
        ],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
