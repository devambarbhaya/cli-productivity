from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "sqlalchemy",
        "plyer"
    ],
    entry_points={
        "console_scripts": [
            "task=cli.__init__:cli",
        ],
    },
)
