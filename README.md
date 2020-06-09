# CLEF2020-CheckThat! Task 5: Check-worthiness for Political Debates 
This repository contains the _dataset_ for the [CLEF2020-CheckThat! task 5](https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0) on Check-wothiness estimation for political debates.
It also contains the _format checker, scorer and baselines_ for the task.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 4.0: Jun 8, 2020 (Data, Baseline, and input-Test Release)
````

The task is part of the CLEF2020-CheckThat Lab on "Automatic Identification and Verification of Claims". The current version includes the training dataset, evaluation scores, baselines and the test files (with gold labels).

__Table of contents:__
* [Evaluation Results](#evaluation-results)
* [List of Versions](#list-of-versions)
* [Contents of the Repository](#contents-of-the-repository)
* [Task Definition](#task-definition)
* [Data Format](#data-format)
* [Results File Format](#results-file-format)
* [Format checker](#format-checker)
* [Scorer](#scorer)
   * [Evaluation metrics](#evaluation-metrics)
* [Baselines](#baselines)
* [Licensing](#licensing)
* [Citation](#citation)
* [Previos Editions](#previous-editions)
* [Credits](#credits)

## Evaluation Results

You can find the results in this spreadsheet, https://tinyurl.com/y9sjooxo.

## List of Versions

* __4.0 [2020/06/08]__ - Test data with gold labels released

* __3.0 [2020/05/26]__ - Input test data released

* __2.0 [2020/05/11]__ - Updated some labels in the training data.

* __v1.0 [2020/03/16]__ -  data. The training data for task 5 contains 50 fact-checked documents - debates, speeches, press conferences, etc. 

## Contents of the Repository

We provide the following files:

- Main folder: [data](data)
  - Subfolder [/training](data/training) <br/>
   Contains all training data released with the version 2.0

  - Subfolder [/test](data/test.zip) <br/>
   Contains all test data wtih gold labels

  - [README.md](README.md) <br/>
    this file
  
  - [working_notes/clef19_checkthat.bib](working_notes/clef19_checkthat.bib) - Bibliography of 2019 overview and participants' papers.
  - [working_notes/clef18_checkthat.bib](working_notes/clef18_checkthat.bib) - Bibliography of 2018 overview and participants' papers.

- Main folder: [test-input](test-input)
  - [test-input.zip](test-input/test-input.zip) <br/>
    File containing 20 debates that will be used for testing contestents' models.
  
## Task Definition 

The "Check-worthines for debates" task is defined as "predicting which claim in a political debate should be prioritized for fact-checking". 
In particular, given a debate, speech or a press conference the goal is to produce a ranked list of its sentences based on their worthiness for fact checking. 

**NOTE:** You can use data from the CLEF-2018 and the CLEF-2019 editions of this task

## Data Format

The input files are TAB-separated CSV files with four fields:

> line_number <TAB> speaker <TAB> text <TAB> label

Where: <br>
* line_number: the line number (starting from 1) <br/>
* speaker: the person speaking (a candidate, the moderator, or "SYSTEM"; the latter is used for the audience reaction) <br/>
* text: a sentence that the speaker said <br/>
* label: 1 if this sentence is to be fact-checked, and 0 otherwise 

The text encoding is UTF-8.

Example:

>  ... <br/>
>  65  TRUMP So we're losing our good jobs, so many of them. 0 <br/>
>  66  TRUMP When you look at what's happening in Mexico, a friend of mine who builds plants said it's the eighth wonder of the world. 0 <br/>
>  67  TRUMP They're building some of the biggest plants anywhere in the world, some of the most sophisticated, some of the best plants. 0 <br/>
>  68  TRUMP With the United States, as he said, not so much.  0 <br/>
>  69  TRUMP So Ford is leaving. 1 <br/> 
>  70  TRUMP You see that, their small car division leaving. 1 <br/>
>  71  TRUMP Thousands of jobs leaving Michigan, leaving Ohio. 1 <br/>
>  72  TRUMP They're all leaving.  0 <br/>
>  ...

## __Results File Format__: 

For this task, the expected results file is a list of claims with the estimated score for check-worthiness. 
    Each row contains two tab-separated fields:
>line_number <TAB> score

Where _line_number_ is the number of the claim in the debate and _score_ is a number, indicating the priority of the claim for fact-checking. For example:
>1	0.9056 <br/>
>2	0.6862 <br/>
>3	0.7665 <br/>
>4	0.9046 <br/>
>5	0.2598 <br/>
>6	0.6357 <br/>
>7	0.9049 <br/>
>8	0.8721 <br/>
>9	0.5729 <br/>
>10	0.1693 <br/>
>11	0.4115 <br/>
> ...

Your result file **MUST contain scores for all lines** of the input file.
Otherwise the scorer will return an error and no score will be computed. 

## Format checker

The checker for the task is located in the [format_checker](format_checker) module of the project.
The format checker verifies that your generated results file complies with the expected format.
To launch it run: 
> python3 format_checker/main.py --pred_file_path=<path_to_your_results_file> <br/>

`run_format_checker.sh` includes examples of the output of the checker when dealing with an ill-formed results file. 
Its output can be seen in [run_format_checker_out.txt](format_checker/run_format_checker_out.txt). 
Note that the checker cannot verify whether the prediction file you submit contain all lines / claims), because it does not have access to the corresponding gold file.

The script used is adapted from the one for the [CLEF2019 Check That! Lab Task 1 (check-worthiness)](https://github.com/apepa/clef2019-factchecking-task1).

## Scorer 

Launch the scorer for the task as follows:
> python3 scorer/main.py --gold_file_path="<path_gold_file_1, path_to_gold_file_k>" --pred_file_path="<predictions_file_1, predictions_file_k>" <br/>

Both `--gold_file_path` and `--pred_file_path` take a single string that contains a comma separated list of file paths. The lists may be of arbitraty positive length (so even a single file path is OK) but their lengths must match.

__<path_to_gold_file_n>__ is the path to the file containing the gold annotations for debate __n__ and __<predictions_file_n>__ is the path to the corresponding file with participants' predictions for debate __n__, which must follow the format, described in the 'Results File Format' section.

The scorer invokes the format checker for the task to verify the output is properly shaped.
It also handles checking if the provided predictions file contains all lines / claims from the gold one.

`run_scorer.sh` provides examples on using the scorers and the results can be viewed in the [run_scorer_out.txt](scorer/run_scorer_out.txt) file.

The script used is adapted from the one for the [CLEF2019 Check That! Lab Task 1 (check-worthiness)](https://github.com/apepa/clef2019-factchecking-task1).

### Evaluation metrics

**The official evaluation measure is Mean Average Precision (MAP)**. 
We also report R-Precision, Average Precision, Recipocal Rank, Precision@k and averaged over multiple debates.

## Baselines

The [baselines](/baselines) module contains a random and a simple ngram baseline for the task.
To launch the baseline script you need to install packages dependencies found in [requirement.txt](requirement.txt) using the following:
> pip3 install -r requirement.txt <br/>

To launch the baseline script run the following:
> python3 baselines/baselines.py  <br/>

Both of the baselines will be trained on all but the latest 20% of the debates as they are used as the dev dataset.
The performance of both baselines will be displayed:<br/>
Random Baseline AVGP: 0.02098366142405398<br/>
Ngram Baseline AVGP: 0.09456735615609717<br/>

The scripts used are adapted from the ones for the [CLEF2019 Check That! Lab Task 1 (check-worthiness)](https://github.com/apepa/clef2019-factchecking-task1).

## Licensing

  These datasets are free for general research use.

## Citation
* If you want to cite any of the papers from the previous edition of the task, refer to this file [working_notes/clef19_checkthat.bib](working_notes/clef19_checkthat.bib) [[PROCEEDINGS WITH ALL PAPERS from 2019]](http://ceur-ws.org/Vol-2125/) or [working_notes/clef18_checkthat.bib](working_notes/clef18_checkthat.bib) [[PROCEEDINGS WITH ALL PAPERS from 2018]](http://ceur-ws.org/Vol-2125/).

## Previous Editions

For information about the previous edition of the shared task, refer to [CLEF2019-CheckThat!](https://sites.google.com/view/clef2019-checkthat/task-1-check-worthiness?authuser=0) and [CLEF2018-CheckThat!](http://alt.qcri.org/clef2018-factcheck/).

## Credits

Task 5 Organizers:

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0

Contact:   clef-factcheck@googlegroups.com

