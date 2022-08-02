from setuptools import setup
from glob import glob
from pathlib import Path


CURRENT_DIR = Path(__file__).parent

long_description = (CURRENT_DIR / "README.md").read_text(encoding="utf8")

description = (
    "PhageAI is an AI-driven software platform using advanced Machine Learning"
    " and Natural Language Processing techniques for deeper understanding of"
    " the bacteriophages genomics."
)

# Read requirements and process as list of strings
dependencies = (CURRENT_DIR / "requirements.txt").read_text()
dependencies = list(map(str.strip, filter(None, dependencies.split("\n"))))


version = "0.4.0"

setup(
    name="phageai",
    version=version,
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="PhageAI S.A.",
    author_email="contact@phage.ai",
    url="https://github.com/phageaisa/phageai",
    download_url=f"https://github.com/phageaisa/phageai/archive/v{version}.tar.gz",
    setup_requires=["setuptools>=50.3.0", "wheel>=0.35.1"],
    install_requires=dependencies,
    packages=[
        "phageai",
        "phageai.repository",
        "phageai.lifecycle",
    ],
    data_files=glob("examples/*/**"),
    include_package_data=True,
    keywords=[
        "bacteriophages",
        "phages",
        "phage therapy",
        "phage research",
        "phage lifecycle",
        "phage taxonomy",
        "virulent phage",
        "temperate phage",
        "chronic phage",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
