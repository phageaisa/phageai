## PhageAI life cycle classifer datasets

### Legend

* `acc_no` - NCBI or GenBank accession number  
* `lifecycle` - Chronic / Non-chronic or Temperate / Virulent life cycle class  
* `train_test` - column with 0 (train) or 1 (test) values

#### Cascade I: train and test split 

**The Chronic train and test set** split was divided into approximately 74% (348) observations in the training and 26% (90) in the testing sets.

**The Non-chronic train and test set** was based on taxonomy and around 69% (2 830) observations were allocated for the model training and 31% (874) for testing.

#### Cascade II: train and test split

**The Virulent vs. Temperate train and test** set was based on taxonomy and 86% (550) observations were allocated for the model training and 14% (91) for testing.

#### Final dataset

As final result, we obtained the dataset consisting of **4 720 bacteriophages** with a confirmed lifecycle. All samples were covered by two CSV files and are available in NCBI.
