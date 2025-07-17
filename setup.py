from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="supaflosho",
    version="1.0.0",
    author="Gregory Reeves (Inkwell Technology Studios) & SupaFloSho Contributors",
    author_email="",
    description="Unified AI-driven development framework combining xText-PRP, SuperClaude, and FloSho",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a2thalex/SupaFloSho",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "supaflosho=setup.install:main",
        ],
    },
    include_package_data=True,
    package_data={
        "supaflosho": [
            ".claude/**/*",
            "templates/**/*",
            "examples/**/*",
        ],
    },
)