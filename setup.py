from setuptools import setup, find_packages

setup(
    name="my_project",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "SQLAlchemy",
        "plyer", # Required for Linux notifications
    ],
    entry_points={
        "console_scripts": [
            "task-cli=cli.__init__:cli",
        ],
    },
    author="Devam Barbhaya",
    description="A CLI-based task management tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
