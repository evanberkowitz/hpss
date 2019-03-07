import setuptools

with open("README.md", "r") as read_me:
    long_description = read_me.read()

setuptools.setup(
    name="hpss",
    version="0.0.1",
    author="Evan Berkowitz",
    author_email="e.berkowitz@fz-juelich.de",
    description="Interface with an HPSS tape archive.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evanberkowitz/hpss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)