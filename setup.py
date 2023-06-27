"""
Author(s): Matthew Loper

See LICENCE.txt for licensing and contact information.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# try: # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError: # for pip <= 9.0.3
#     from pip.req import parse_requirements
# from runpy import run_path

# install_reqs = parse_requirements('requirements.txt', session=False)
# try:  # for pip < 20.1
#     install_requires = [str(ir.req) for ir in install_reqs]
# except AttributeError:  # for pip >= 20.1
#     install_requires = [str(ir.requirement) for ir in install_reqs]
#     print(install_requires, type(install_requires[0]))

def get_version():
    namespace = run_path('chumpy/version.py')
    print(namespace['version'],type(namespace['version']))
    return namespace['version']


setuptools.setup(
    name="chumpy",
    version=get_version(),
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

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'
    ],
)
