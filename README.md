<p align="center">
  <img src="https://phage.ai/assets/images/phageai_logo2.svg">
</p>

**PhageAI** is an application that simultaneously represents **a repository of knowledge of bacteriophages** and a tool to analyse genomes with **Artificial Intelligence support**. This package supports the most critical programmable features from our platform.

Machine Learning algorithms can process enormous amounts of data in relatively short time in order to find connections and dependencies that are unobvious for human beings. Correctly designed applications based on AI are able to vastly improve and speed up the work of the domain experts.

Models based on DNA contextual vectorization and Deep Neural Networks are particularly effective when it comes to analysis of genomic data. The system that we propose aims to use the phages sequences uploaded to the database to build a model which is able to predict if a bacteriophage is **chronic**, **temperate** or **virulent** with a high probability.

One of the key system modules is the bacteriophages repository with a clean web interface that allows to browse, upload and share data with other users. The gathered knowledge about the bacteriophages is not only valuable on its own but also because of the ability to train the ever-improving Machine Learning models.

Detection of virulent or temperate features is only one of the first tasks that can be solved with Artificial Intelligence. The combination of Biology, Natural Language Processing and Machine Learning allows us to create algorithms for genomic data processing that could eventually turn out to be effective in a wide range of problems with focus on classification and information extraced from DNA.


[![PyPI version](https://img.shields.io/pypi/v/phageai.svg)](https://pypi.org/project/phageai/)
[![PyPI license](https://img.shields.io/pypi/l/phageai.svg)](https://pypi.python.org/pypi/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/phageai.svg)](https://pypi.python.org/pypi/phageai/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/phageai)](https://pepy.tech/project/phageai)
[![Twitter Follow](https://img.shields.io/twitter/follow/phageai.svg?style=social)](https://twitter.com/phageai)
[![LinkedIn Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=appveyor)](https://pl.linkedin.com/company/phageai-s-a)


## Table of Contents

[Framework modules](https://github.com/phageaisa/phageai#framework-modules) | [Installation](https://github.com/phageaisa/phageai#installation-and-usage) | [Benchmark](https://github.com/phageaisa/phageai#benchmark) | [Community and Contributions](https://github.com/phageaisa/phageai#community-and-contributions) | [Have a question?](https://github.com/phageaisa/phageai#have-a-question) | [Found a bug?](https://github.com/phageaisa/phageai#found-a-bug) | [Team](https://github.com/phageaisa/phageai#team) | [Change log](https://github.com/phageaisa/phageai#change-log) | [License](https://github.com/phageaisa/phageai#license) | [Cite](https://github.com/phageaisa/phageai#cite)

## Framework modules

Set of methods related with:
* `lifecycle` - bacteriophage lifecycle prediction:
  * `.predict(fasta_path)` - return bacteriophage lifecycle prediction class (Virulent, Temperate or Chronic) with probability (%);
* `taxonomy` - bacteriophage taxonomy order, family and genus prediction (TBA);
* `topology` - bacteriophage genome topology prediction (TBA);
* `repository` - set of methods related with PhageAI bacteriophage repository:
  * `.get_record(value)` - return dict with Bacteriophage meta-data
  * `.get_top10_similar_phages(value)` - return list of dicts contained top-10 most similar bacteriophages

## Installation and usage

#### PhageAI user account (1/3)
Create a free user account in [the PhageAI web platform](https://app.phage.ai/) or use an existing one. If you had to create new one, activate your account by activation link which was sent on your mail inbox. After that, log into the platform successfully and click "My profile" in the top-right menu. In the "API access" section create a new access token (string) and copy it for the steps below.

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
pip install git+https://github.com/phageaisa/phageai.git@develop
```

#### PhageAI execution (3/3)

`PASTE_YOUR_ACCESS_TOKEN_HERE` - PhageAI web user's access token;
`PASTE_YOUR_FASTA_PATH_HERE` - FASTA filename with *.fasta or *.fa extension;

### Example I - single phage prediction

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

If you reach out your daily requests limit, and you still need more, feel free to contact us by contact@phageai.

### Example II - prediction for directory with phages

```python
import os
import csv
from pathlib import Path

from phageai.lifecycle.classifier import LifeCycleClassifier

lcc = LifeCycleClassifier(access_token='PASTE_YOUR_ACCESS_TOKEN_HERE')

# Be aware that directory have to includes *.fasta files only
phage_dir_path = Path('PASTE_YOUR_DIRECTORY_NAME_WITH_FASTA_FILES')
phage_directory = os.listdir(phage_dir_path)

prediction_results = {}

for single_fasta_file in phage_directory:
    try:
        prediction_results[single_fasta_file] = lcc.predict(fasta_path=phage_dir_path / single_fasta_file)
    except Exception as e:
        print(f'[PhageAI] Phage {single_fasta_file} raised an exception "{e}"')

# Python dict with prediction results
for fasta, phageai in prediction_results.items():
    print(fasta, phageai)

# Prepare CSV report as a final result
csv_columns = [
    'fasta_name', 'model_class_label', 'prediction_accuracy',
    'gc', 'sequence_length'
]

# CSV file name
csv_file = "phageai_report.csv"

with open(csv_file, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()

    for fasta_name, phage_data in zip(prediction_results.keys(), prediction_results.values()):
        phage_data["fasta_name"] = fasta_name
        writer.writerow(phage_data)
```

### Example III - get bacteriophage meta-data and top-10 similar samples from PhageAI

```python
from phageai.repository.phages import BacteriophageRepository

phageai_repo = BacteriophageRepository(access_token='PASTE_YOUR_ACCESS_TOKEN_HERE')

# Get bacteriophage meta-data based on accession number (or hash value)
# It can return one or more than one results
phageai_repo.get_record(value='MZ375324')

# Get top 10 similar bacteriophage samples
phageai_repo.get_top10_similar_phages(value='MZ375324')
```

We will share numerous examples of using the package in Jupyter Notebook format (*.ipynb) soon.

## Benchmark

PhageAI lifecycle classifier was benchmarked with [DeePhage](https://github.com/shufangwu/DeePhage), [bacphlip](https://github.com/adamhockenberry/bacphlip), [VIBRANT](https://github.com/AnantharamanLab/VIBRANT) and [PHACTS](https://github.com/deprekate/PHACTS) tools using 91 Virulent and Temperate bacteriophages from our paper (testing set). Correct predictions results:

Tool | Version | Chronic support | No. viruses' genomes | Test set accuracy | DOI |
--- | --- | --- | --- | --- | --- |
**PhageAI** | **1.5** | **Yes** | **17 559** | **98,90** | **This research** |
DeePhage | 1.0 | No | 1 640 | N/A | 10.1093/gigascience/giab056 |
bacphlip | 0.9.6 | No | 1 057 | 100 | 10.7717/peerj.11396 |
VIBRANT | 1.2.1 | No | 350 626 | 92,31 | 10.1186/s40168-020-00867-0 |
PHACTS | 0.3 | No | 227 | 89,13 | 10.1093/bioinformatics/bts014 |

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
* Krzysztof Owsieniuk
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
