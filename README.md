<p align="center">
  <img src="https://phage.ai/assets/images/phageai_logo2.svg">
</p>

**PhageAI** is an application that simultaneously represents **a repository of knowledge of bacteriophages** and a bioinformatics pipeline to analyse genomes with **Artificial Intelligence support**. This package supports the most critical programmable features from our platform.

Machine Learning algorithms can process enormous amounts of data in relatively short time in order to find connections and dependencies that are obvious for human beings. Correctly designed applications based on AI are able to vastly improve and speed up the work of the domain experts.

Models based on DNA or proteins contextual vectorization and Deep Neural Networks are particularly effective when it comes to analysis of genomic data. The system that we propose aims to use the phages sequences uploaded to the database to build a model which is able to predict if a bacteriophage is **chronic**, **temperate** or **virulent** with a high probability. Furthermore, our system shares more prediction methods for phage taxonomy, phage similarity and annotation extended by proteins structural classes classification.

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

[Available methods](https://github.com/phageaisa/phageai#available-methods) | [Installation](https://github.com/phageaisa/phageai#installation-and-usage) | [Benchmark](https://github.com/phageaisa/phageai#benchmark) | [Community and Contributions](https://github.com/phageaisa/phageai#community-and-contributions) | [Have a question?](https://github.com/phageaisa/phageai#have-a-question) | [Found a bug?](https://github.com/phageaisa/phageai#found-a-bug) | [Team](https://github.com/phageaisa/phageai#team) | [Change log](https://github.com/phageaisa/phageai#change-log) | [License](https://github.com/phageaisa/phageai#license) | [Cite](https://github.com/phageaisa/phageai#cite)

## Available methods

* `upload(fasta_path, access)` - upload FASTA file with phage genome as "public", "private" or "" (temporary) sample in the PhageAI repository. Upload stage is starting the bioinformatics pipeline execution for phage characteristic.
* `processing_status(job_id)` - get current processing status for your phage sample related with Job ID;
* `get_lifecycle_classification(job_id)` - get phage lifecycle classification result;
* `get_taxonomy_classification(job_id)` - get phage taxonomy classification results for order, family and genus;
* `get_proteins_classification(job_id)` - get phage proteins structural classes classification results;
* `get_top10_similarities(job_id)` - get TOP-10 similar phages to your sample from the repository;
* `get_full_report(job_id)` - get full phage characteristics report (all meta-data and predictions);
* `get_phage_characteristic(accession_number)` - get meta-data about publicly available phage with specific accession number (with version);


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

### Example - how to upload phage to repository with private access

```python
from phageai.platform import PhageAIAccounts

phageai_api = PhageAIAccounts(access_token='PASTE_YOUR_ACCESS_TOKEN_HERE')

phage_example_jobid = phageai_api.upload(fasta_path="PASTE_YOUR_FASTA_PATH_HERE", access="private")
```

Expected output should be the job ID value:
```json
{
  'job_id': '0a71e61a-ec58-447b-859e-d9ba15e103a9'
}
```

or, if you reach out daily API requests limit (100 by default), you can expect:

```json
{
    "author": ["Your daily API limit (100 requests) has been exceeded"]
}
```

If you reach out your daily requests limit, and you still need more, feel free to contact us by contact@phageai.

### Example - how to track the processing progress

Tracking progress of phage processing is super useful if you upload more samples in the same time or when you integrate your service or pipeline with PhageAI.

```python
(...)

phage_example_jobid = phageai_api.upload(fasta_path="PASTE_YOUR_FASTA_PATH_HERE", access="private")

job_id = phage_example_jobid["job_id"]

phageai_api.processing_status(job_id=job_id)
```

Depends on what is the current stage of your sample processing ("Not Started", "In progress", "Done", "Failed"), expected output should be like:

```python
{
  'taxonomy_stage': 'Done',
  'proteins_stage': 'Not Started',
  'top10_stage': 'Not Started',
  'lifecycle_stage': 'Done',
  'final_report': 'In Progress'
}
```

Each of the above stage is work separately in PhageAI so you can expect different statuses for each of them.

### Example - get lifecycle classification

```python
(...)

phageai_api.get_lifecycle_classification(job_id=job_id)
```

Expected output should be like:

```python
{'value': 'Chronic', 'probability': 99.85}
```

In the same way you can execute other [available methods](https://github.com/phageaisa/phageai#available-methods) from the package. 

## Benchmark

PhageAI lifecycle classifier was benchmarked with [DeePhage](https://github.com/shufangwu/DeePhage), [bacphlip](https://github.com/adamhockenberry/bacphlip), [VIBRANT](https://github.com/AnantharamanLab/VIBRANT) and [PHACTS](https://github.com/deprekate/PHACTS) tools using 104 Virulent and Temperate bacteriophages from our paper (testing set). Correct predictions results:

Tool | Version   | Chronic support | Phage sequences used in research | Test set accuracy (%) | DOI |
--- |-----------| --- |----------------------------------|-----------------------| --- |
**PhageAI** | **0.4.1** | **Yes** | **15,235**                       | **93.27**             | **This research** |
DeePhage | 1.0       | No | 1,640                            | 84.62                 | 10.1093/gigascience/giab056 |
bacphlip | 0.9.6     | No | 1,057                            | 100                   | 10.7717/peerj.11396 |
VIBRANT | 1.2.1     | No | 350,626                          | 85.58                 | 10.1186/s40168-020-00867-0 |
PHACTS | 1.8       | No | 227                              | 75.00                 | 10.1093/bioinformatics/bts014 |

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
* Żaneta Szulc
* Maria Urbanowicz

## Change log

The log's will become rather long. It moved to its own file.

See [CHANGELOG.md](https://github.com/phageaisa/phageai/blob/master/CHANGELOG.md).

## License

The PhageAI package is released under the under terms of [the MIT License](https://github.com/phageaisa/phageai/blob/master/LICENSE).

## Cite

> **PhageAI - Bacteriophage Life Cycle Recognition with Machine Learning and Natural Language Processing**
>
> Tynecki, P.; Guziński, A.; Kazimierczak J.; Zimoń B.; Szulc Ż.; Jadczuk, M.; Dastych, J.; Onisko, A.
>
> Viruses, Special Issue "Bacteriophage Bioinformatics"
(ISSN 1999-4915), DOI: [10.1101/2020.07.11.198606](https://doi.org/10.1101/2020.07.11.198606)
