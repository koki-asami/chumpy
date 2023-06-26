import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="chumpy", # Replace with your own username
    version="0.40",
    install_requires = [
        "numpy>=1.8.1",
        "scipy>=0.13.0",
        "six>=1.11.0",
    ],
    author="Matthew Loper",
    author_email="matt.loper@gmail.com",
    description="chumpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattloper/chumpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
