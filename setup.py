from setuptools import setup, find_packages

setup(
    name="AdamSDK",
    version="0.1.0",
    author="Prometu",
    author_email="info@prometu.com",
    description="SDK for controlling Adam, the robot by Prometu, with capabilities to interact with various sensors, control the camera, manage AI assistant functionalities, and more.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prometuinc/adam-sdk",
    packages=find_packages(where='adam-sdk'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
