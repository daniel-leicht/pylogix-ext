import setuptools

with open("README", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="pylogix2",
    version="0.5.3",
    author="Daniel Leicht",
    author_email="daniel.leicht@gmail.com",
    description="Read/Write Rockwell Automation Logix based PLCs",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="Apache License 2.0",
    url="https://github.com/daniel-leicht/pylogix2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        ],
    )
