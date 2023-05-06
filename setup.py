from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = "A personal use utils for torch"

setup(
    name="z_dlutils",
    version=VERSION,
    author="crafter-z",
    author_email="crafterz@163.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["torch", "matplotlib", "opencv-python"],
    keywords=["torch", "utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
