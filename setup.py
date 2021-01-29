from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="average_price",
    version="1.0.0",
    author="Tibor Reiss",
    author_email="tibor.reiss@gmail.com",
    description="Real-time average price calculator for instruments with 1..n different markets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tibor-reiss/average_price",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'aiosqlite',
        'databases',
    ],
    python_requires='>=3.8',
)
