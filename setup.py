#!/usr/bin/env python3
"""
SupaFloSho Setup Script
For Python package installation
"""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="supaflosho",
    version="1.0.0",
    author="SupaFloSho Contributors",
    author_email="dev@supaflosho.ai",
    description="Unified AI-driven development framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a2thalex/SupaFloSho",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: JavaScript",
    ],
    python_requires=">=3.7",
    install_requires=[
        "colorama>=0.4.6",
        "pyyaml>=6.0",
        "packaging>=23.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "supaflosho=setup.install:main",
            "sfs=setup.install:main",  # Short alias
        ],
    },
    include_package_data=True,
    package_data={
        "supaflosho": [
            "templates/**/*",
            "examples/**/*",
            ".claude/**/*",
            "core/**/*",
            "testing/**/*",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/a2thalex/SupaFloSho/issues",
        "Source": "https://github.com/a2thalex/SupaFloSho",
        "Documentation": "https://supaflosho.ai/docs",
    },
)