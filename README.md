<p align="center">
  <img src="https://raw.githubusercontent.com/phageaisa/phageai/main/media/phageai.jpeg">
</p>

**PhageAI** is an application that simultaneously represents **a repository of knowledge of bacteriophages** and a tool to analyse genomes with **Artificial Intelligence support**. This package supports the most critical programmable features from our platform.  

Machine Learning algorithms can process enormous amounts of data in relatively short time in order to find connections and dependencies that are unobvious for human beings. Correctly designed applications based on AI are able to vastly improve and speed up the work of the domain experts.  

Models based on DNA contextual vectorization and Deep Neural Networks are particularly effective when it comes to analysis of genomic data. The system that we propose aims to use the phages sequences uploaded to the database to build a model which is able to predict if a bacteriophage is **chronic**, **temperate** or **virulent** with a high probability.  

One of the key system modules is the bacteriophages repository with a clean web interface that allows to browse, upload and share data with other users. The gathered knowledge about the bacteriophages is not only valuable on its own but also because of the ability to train the ever-improving Machine Learning models.  

Detection of virulent or temperate features is only one of the first tasks that can be solved with Artificial Intelligence. The combination of Biology, Natural Language Processing and Machine Learning allows us to create algorithms for genomic data processing that could eventually turn out to be effective in a wide range of problems with focus on classification and information extraced from DNA.  
  

[![Travis CI](https://travis-ci.com/ProteonPharmaceuticals/phageai.svg?branch=main)](https://travis-ci.com/github/ProteonPharmaceuticals/phageai)
[![codecov](https://codecov.io/gh/ProteonPharmaceuticals/phageai/branch/master/graph/badge.svg)](https://codecov.io/gh/ProteonPharmaceuticals/phageai)
[![Documentation Status](https://readthedocs.org/projects/phageai/badge/?version=stable)](https://phageai.readthedocs.io/en/stable/?badge=stable)
[![PyPI version](https://img.shields.io/pypi/v/phageai.svg)](https://pypi.org/project/phageai/)
[![PyPI license](https://img.shields.io/pypi/l/phageai.svg)](https://pypi.python.org/pypi/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/phageai.svg)](https://pypi.python.org/pypi/phageai/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/phageai)](https://pepy.tech/project/phageai)
[![Twitter Follow](https://img.shields.io/twitter/follow/phageai.svg?style=social)](https://twitter.com/phageai) 


## Table of Contents

[Framework modules](https://github.com/phageaisa/phageai#framework-modules) | [Documentation](https://github.com/phageaisa/phageai#documentation) | [Installation](https://github.com/phageaisa/phageai#installation-and-usage) | [Benchmark](https://github.com/phageaisa/phageai#benchmark) | [Community and Contributions](https://github.com/phageaisa/phageai#community-and-contributions) | [Have a question?](https://github.com/phageaisa/phageai#have-a-question) | [Found a bug?](https://github.com/phageaisa/phageai#found-a-bug) | [Team](https://github.com/phageaisa/phageai#team) | [Change log](https://github.com/phageaisa/phageai#change-log) | [License](https://github.com/phageaisa/phageai#license) | [Cite](https://github.com/phageaisa/phageai#cite)

## Framework modules

Set of methods related with:
* `lifecycle` - bacteriophage lifecycle prediction;  
* `taxonomy` - bacteriophage taxonomy order, family and genus prediction (TBA);  
* `topology` - bacteriophage genome topology prediction (TBA);  
* `repository` - set of methods related with PhageAI bacteriophage repository (TBA); 

## Documentation

The official technical documentation is hosted on ReadTheDocs: https://phageai.readthedocs.io

## Installation and usage

#### PhageAI user account (1/3)
Create a free user account in [the PhageAI web platform](https://phage.ai/) or use an existing one. If you had to create new one, activate your account by activation link which was sent on your mail inbox. After that, log into the platform successfully and click "My profile" on menu (left sidebar). From the "API access" section copy the access token (string) and keep it for the steps below.

<p align="center">
  <img src="https://raw.githubusercontent.com/phageaisa/phageai/main/media/phageai-access-token.png">
</p>

#### PhageAI package (2/3)

_PhageAI_ requires Python 3.8.0+ to run and can be installed by running:

```
pip install phageai
```

If you can't wait for the latest hotness from the develop branch, then install it directly from the repository:

```
pip install git+git://github.com/phageaisa/phageai.git@develop
```

#### PhageAI execution (3/3)

`PASTE_YOUR_ACCESS_TOKEN_HERE` - PhageAI web user's access token;  
`PASTE_YOUR_FASTA_PATH_HERE` - FASTA filename with *.fasta or *.fa extension;


```python
from phageai.lifecycle.classifier import LifeCycleClassifier

lcc = LifeCycleClassifier(access_token='PASTE_YOUR_ACCESS_TOKEN_HERE')
lcc.predict(fasta_path='PASTE_YOUR_FASTA_PATH_HERE')
```

Expected output for `MG945357.fasta` bacateriophage sample:
```json
{
    "model_class_label": "Virulent",
    "prediction_accuracy": "98.94",
    "gc": "39.47",
    "sequence_length": 4915
}
```

or, if you reach out daily API requests limit, you can expect:

```json
{
    "author": ["Your daily API limit (100 requests) has been exceeded"]
}
```

We will share numerous examples of using the package in Jupyter Notebook format (*.ipynb) soon.

## Benchmark

PhageAI lifecycle classifier was benchmarked with [PHACTS](https://github.com/deprekate/PHACTS), [VIBRANT](https://github.com/AnantharamanLab/VIBRANT) and [bacphlip](https://github.com/adamhockenberry/bacphlip) tools using 81 bacteriophages from our paper (testing set). Correct predictions results:

Classifier | Version | Correct | Invalid | Score |
--- | --- | --- | --- | --- |
**PhageAI** | **1.3** | **81** | **0** | **100%** |
bacphlip | 0.9.6 | 80 | 1 | 99% |
VIBRANT | 1.2.1 | 76 | 5 | 94% |
PHACTS | Unknown | 73 | 8 | 90% |

Full comparison report is [available here](https://raw.githubusercontent.com/phageaisa/phageai/main/media/phageai-81-testset-phages-benchmark-03.12.2020.xlsx) (as XLSX).  

## Community and Contributions

Happy to see you willing to make the PhageAI better. Development on the latest stable version of Python 3+ is preferred. As of this writing it's 3.8. You can use any operating system.

If you're fixing a bug or adding a new feature, add a test with *[pytest](https://github.com/pytest-dev/pytest)* and check the code with *[Black](https://github.com/psf/black/)* and *[mypy](https://github.com/python/mypy)*. Before adding any large feature, first open an issue for us to discuss the idea with the core devs and community.

## Have a question?

Obviously if you have a private question or want to cooperate with us, you can always reach out to us directly by mail.

## Found a bug?

Feel free to add a new issue with a respective title and description on the [the PhageAI repository](https://github.com/phageaisa/phageai/issues). If you already found a solution to your problem, we would be happy to review your pull request.

## Team

Core Developers and Domain Experts who contributing to PhageAI:

* Piotr Tynecki
* Łukasz Wałejko
* Joanna Kazimierczak
* Arkadiusz Guziński
* Bogumił Zimoń

## Change log

The log's will become rather long. It moved to its own file.

See [CHANGELOG.md](https://github.com/phageaisa/phageai/blob/master/CHANGELOG.md).

## License

The PhageAI package is released under the under terms of [the MIT License](https://github.com/phageaisa/phageai/blob/master/LICENSE).

## Cite

> **PhageAI - Bacteriophage Life Cycle Recognition with Machine Learning and Natural Language Processing**  
>
> Tynecki, P.; Guziński, A.; Kazimierczak, J.; Jadczuk, M.; Dastych, J.; Onisko, A.
>
> Bioinformatics 2020, DOI: [10.1101/2020.07.11.198606](https://doi.org/10.1101/2020.07.11.198606)
