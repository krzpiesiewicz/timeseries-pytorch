import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timeseries-pytorch",
    version="0.0.2",
    author="Krzysztof Piesiewicz",
    author_email="krz.piesiewicz@gmail.com",
    description="A pytorch extension for timeseries package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krzpiesiewicz/timeseries-pytorch",
    packages=setuptools.find_packages(exclude=['tests', 'examples']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    dependency_links=[
        "https://github.com/krzpiesiewicz/pytorch-fit#egg=pytorch_fit",
        "https://github.com/krzpiesiewicz/timeseries#egg=timeseries",
    ],
    install_requires=[
        "pandas>=1.0.5",
        "numpy>=1.19.0",
        "torch>=1.8.0"
    ],
    test_requirements=["pytest>=6.2.0"],
    python_requires='>=3.6',
)
