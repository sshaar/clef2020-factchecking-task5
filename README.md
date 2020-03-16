# CLEF2020-CheckThat! Task 5
This repository contains the _dataset_ for the [CLEF2020-CheckThat! task 5](https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0).

For information about the previous edition of the shared task, refer to [CLEF2019-CheckThat!](http://alt.qcri.org/clef2019-factcheck/) and [CLEF2018-CheckThat!](http://alt.qcri.org/clef2018-factcheck/).

It also contains the _format checker, scorer and baselines_ for the task.

````
FCPD corpus for the CLEF-2020 LAB on "Automatic Identification and Verification of Claims"
Version 1.0: March ?, 2020 (Data and Baseline Resealse)
````

This file contains the basic information regarding the CLEF2020-CheckThat! Task 5
on Check-Worthiness estimation dataset provided for the CLEF2020-CheckThat Lab
on "Automatic Identification and Verification of Claims".
The current version (1.0, March ?, 2020) corresponds to the release of a 
part of the training data set.
The test set will be provided in future versions.
All changes and updates on these data sets and tools are reported in Section 1 of this document.

__Table of contents:__
* [Evaluation Results](#evaluation-results)
* [List of Versions](#list-of-versions)
* [Contents of the Distribution v1.0](#contents-of-the-distribution-v10)
* [Subtasks](#subtasks)
* [Data Format](#data-format)
* [Results File Format](#results-file-format)
* [Format checkers](#format-checkers)
* [Scorers](#scorers)
   * [Evaluation metrics](#evaluation-metrics)
* [Baselines](#baselines)
* [Notes](#notes)
* [Licensing](#licensing)
* [Citation](#citation)
* [Credits](#credits)

## Evaluation Results

TBA

## List of Versions

* __v1.0 [2020/03/?]__ -  data. The training data for task 5 contains 50 fact-checked documents - debates, speeches, press conferences, etc, analysed by politifact.com. 

## Contents of the Distribution v1.0

We provide the following files:

- Main folder: [data](data)
  - Subfolder [/training](data/training) <br/>
   Contains all training data released with the version 1.0

  - [README.md](README.md) <br/>
    this file
  
  - [working_notes/clef19_checkthat.bib](working_notes/clef19_checkthat.bib) - Bibliography of 2019 overview and participants' papers.
  - [working_notes/clef18_checkthat.bib](working_notes/clef18_checkthat.bib) - Bibliography of 2018 overview and participants' papers.
  
## Subtask 5 : __Debate Check-Worthiness__. 

Predict which claim in a political debate should be prioritized for fact-checking. In particular, given a debate, speech or a press conference the goal is to produce a ranked list of its sentences based on their worthiness for fact checking.

## Data Format

The input files are TAB separated csv files with three fields:

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

Your result file **MUST contain scores for all lines** from the respective input file.
Otherwise the scorer will not score this result file.

## Format checkers

The checker for the subtask is located in the [format_checker](format_checker) module of the project.
The format checker verifies that your generated results file complies with the expected format.
To launch it run: 
> python3 format_checker/main.py --pred_file_path=<path_to_your_results_file> <br/>

`run_format_checker.sh` includes examples of the output of the checker when dealing with an ill-formed results file. 
Its output can be seen in [run_format_checker_out.txt](format_checker/run_format_checker_out.txt)
The checks for completness (if the result files contain all lines / claims) is NOT handled by the format checkers, because they receive only the results file and not the gold one.

## Scorers 

Launch the scorers for the task as follows:
> python3 scorer/main.py --gold_file_path="<path_gold_file_1, path_to_gold_file_k>" --pred_file_path="<predictions_file_1, predictions_file_k>" <br/>

Both `--gold_file_path` and `--pred_file_path` take a single string that contains a comma separated list of file paths. The lists may be of arbitraty positive length (so even a single file path is OK) but their lengths must match.

__<path_to_gold_file_n>__ is the path to the file containing the gold annotations for debate __n__ and __<predictions_file_n>__ is the path to the respective file holding predicted results for debate __n__, which must follow the format, described in the 'Results File Format' section.

The scorers call the format checkers for the task to verify the output is properly shaped.
They also handle checking if the provided predictions file contains all lines / claims from the gold one.

`run_scorer.sh` provides examples on using the scorers and the results can be viewed in the [run_scorer_out.txt](scorer/run_scorer_out.txt) file.

### Evaluation metrics

For Task 5 (ranking): R-Precision, Average Precision, Recipocal Rank, Precision@k and means of these over multiple debates.
**The official metric for task5, that will be used for the competition ranking is the Mean Average Precision (MAP)**

## Baselines

The [baselines](/baselines) module contains a random and a simple ngram baseline for the task.
To launch the baseline script use the following:

> python3 baselines/baselines.py  <br/>

Both of the baselines will be trained on all but the latest 20% of the debates as they are used as the dev dataset.
The performance of both baselines will be displayed:
Random Baseline AVGP: 0.02098366142405398
Ngram Baseline AVGP: 0.09456735615609717

## Licensing

  These datasets are free for general research use.

## Citation
* If you want to cite any of the papers from the previous edition of the task, refer to this file [working_notes/clef18_checkthat.bib](working_notes/clef18_checkthat.bib). [[PROCEEDINGS WITH ALL PAPERS from 2018]](http://ceur-ws.org/Vol-2125/) or [working_notes/clef19_checkthat.bib](working_notes/clef19_checkthat.bib). [[PROCEEDINGS WITH ALL PAPERS from 2019]](http://ceur-ws.org/Vol-2125/)


## Credits

Task 5 Organizers:

* Shaden Shaar, Qatar Computing Research Institute, HBKU <br/>

* Giovanni Da San Martino, Qatar Computing Research Institute, HBKU <br/>

* Pepa Atanasova, University of Copenhagen <br/>

* Preslav Nakov, Qatar Computing Research Institute, HBKU <br/>

Task website: https://sites.google.com/view/clef2020-checkthat/tasks/tasks-1-5-check-worthiness?authuser=0

Contact:   clef-factcheck@googlegroups.com

