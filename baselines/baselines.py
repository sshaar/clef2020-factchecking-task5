import pdb
import pandas as pd
import random
import numpy as np
import os
from os import listdir
from os.path import join, dirname

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

import sys
sys.path.append('.')

from scorer.main import evaluate
from format_checker.main import check_format

import requests, time
from functools import reduce

random.seed(0)
_COL_NAMES = ['line_number', 'speaker', 'text', 'label']
ROOT_DIR = dirname(dirname(__file__))


def run_random_baseline(train_debates):
    for gold_fpath in train_debates:
        results_fpath = join(ROOT_DIR, 'baselines/data/task5_random_baseline_%s'%(os.path.basename(gold_fpath)))
        gold_df = pd.read_csv(gold_fpath, names=_COL_NAMES, sep='\t')
        with open(results_fpath, "w") as results_file:
            for i, line in gold_df.iterrows():
                results_file.write('{}\t{}\n'.format(line['line_number'], random.random()))


def run_ngram_baseline(train_debates, test_debates):

    train_list = []
    for train_debate in train_debates:
        df = pd.read_csv(train_debate, index_col=None, header=None, names=_COL_NAMES, sep='\t')
        train_list.append(df)
    train_df = pd.concat(train_list)

    test_list = []
    for train_debate in test_debates:
        df = pd.read_csv(train_debate, index_col=None, header=None, names=_COL_NAMES, sep='\t')
        test_list.append(df)
    test_df = pd.concat(test_list)

    pipeline = Pipeline([
        ('ngrams', TfidfVectorizer(ngram_range=(1, 1))),
        ('clf', SVC(C=1, gamma=0.75, kernel='rbf', random_state=0))
    ])
    pipeline.fit(train_df['text'], train_df['label'])
    for test_debate in test_debates:
        test_df = pd.read_csv(test_debate, names=_COL_NAMES, sep='\t')
        results_fpath = join(ROOT_DIR, 'baselines/data/task5_ngram_baseline_%s'%(os.path.basename(test_debate)))
        with open(results_fpath, "w") as results_file:
            predicted_distance = pipeline.decision_function(test_df['text'])
            for line_num, dist in zip(test_df['line_number'], predicted_distance):
                results_file.write("{}\t{}\n".format(line_num, dist))


def run_baselines():

    gold_data_folder = join(ROOT_DIR, 'data/training/')
    gold_data_folder = [join(gold_data_folder, debate_name) for debate_name in listdir(gold_data_folder)]
    gold_data_folder.sort()
    
    n_train = int(.8 *len(gold_data_folder))
    train_debates = gold_data_folder[:n_train]
    dev_debates = gold_data_folder[n_train:]

    run_random_baseline(dev_debates)
    avg_precisions = []
    for test_debate in dev_debates:
        random_baseline_fpath = join(ROOT_DIR, 'baselines/data/task5_random_baseline_%s'%(os.path.basename(test_debate)))
        if check_format(random_baseline_fpath):
            thresholds, precisions, avg_precision, reciprocal_rank, num_relevant = evaluate(test_debate, random_baseline_fpath)
            avg_precisions.append(avg_precision)
    print("Random Baseline AVGP:", np.mean(avg_precisions))

    run_ngram_baseline(train_debates, dev_debates)
    avg_precisions = []
    for test_debate in dev_debates:
        ngram_baseline_fpath = join(ROOT_DIR, 'baselines/data/task5_ngram_baseline_%s'%(os.path.basename(test_debate)))
        if check_format(ngram_baseline_fpath):
            thresholds, precisions, avg_precision, reciprocal_rank, num_relevant = evaluate(test_debate, ngram_baseline_fpath)
            avg_precisions.append(avg_precision)
    print("Ngram Baseline AVGP:", np.mean(avg_precisions))


if __name__ == '__main__':
    run_baselines()
