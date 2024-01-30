from setuptools import setup, find_packages

setup(
    name='pypkgs',
    version='0.1.0',
    description="An all-in-one package containing a collection of self-implemented Python packages/frameworks/libraries (the following will collectively be known as 'library') such that you can add this into a project as a submodule and you can import the libraries directly",
    author='Thanatisia',
    author_email='55834101+Thanatisia@users.noreply.github.com',
    packages=find_packages(),
    package_dir={'pypkgs':'pypkgs'},
    install_requires=[
        # List your dependencies here
    ],
    url='https://github.com/Thanatisia/python-pkgs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
    ],
)
