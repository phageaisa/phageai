## Embedding dataset

This directory contains **15,235** bacteriophages used during the embedding model training (Word2Vec model).

## PhageAI life cycle classifer datasets

### Legend

* `acc_no` - NCBI or GenBank accession number (if exists)
* `hash` - unique phage ID from PhageAI repository
* `lifecycle` - Chronic / Non-chronic or Temperate / Virulent life cycle class
* `train_test` - column with 0 (train) or 1 (test) values
* `strandedness` - column with dsDNA, ssDNA values
* `length` - genome size
* `gc` - GC-content (%)

#### Cascade I: train and test split

**Chronic and Non-Chronic** phages were splitted on train set and test set with maintenance of class proportion. 80% (1,703) observations were allocated for the model training and 20% (426) for testing.

#### Cascade II: train and test split

**Temperate and virulent** phages were splitted on train set and test set with maintenance of class proportion. 80% (412) observations were allocated for the model training and 20% (104) for testing.

#### Final dataset

As final result, we obtained the dataset consisting of **2,645 bacteriophages** with a confirmed lifecycle. All samples were covered by two CSV files and are available in NCBI.

## How to download FASTA files?

Feel free to use [PhageAI platform](https://app.phage.ai/) with our bacteriophages repository to get all the samples as FASTA files.
