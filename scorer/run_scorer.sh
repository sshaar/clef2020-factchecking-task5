#!/usr/bin/env bash
PROJ_DIR="$(dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))"
export PYTHONPATH=${PROJ_DIR}
scorer_tests_path=${PROJ_DIR}'/scorer/data/'
gold_file_task5=${PROJ_DIR}/data/training/'20160926_1pres.tsv'

echo 'Scoring a random baseline for task 5'
python3 task5.py --gold_file_path=${gold_file_task5} --pred_file_path=${scorer_tests_path}task5_random_baseline.txt
echo '**********'
echo 'Scoring the gold predictions for task 5'
python3 task5.py --gold_file_path=${gold_file_task5} --pred_file_path=${scorer_tests_path}task5_gold.txt
echo '**********'
echo 'Scoring BOTH the gold and random baseline for task 5 (only for example purposes, scoring multiple files for 1 debate will lead to wrong metrics)'
python3 task5.py --gold_file_path="${gold_file_task5}, ${gold_file_task5}" --pred_file_path="${scorer_tests_path}task5_gold.txt, ${scorer_tests_path}task5_random_baseline.txt"
echo '**********'
echo 'TEST ERROR: Scoring task 5, where the provided list of line_numbers contains a line_number, which is not in the gold file.'
python3 task5.py --gold_file_path=${gold_file_task5} --pred_file_path=${scorer_tests_path}task5_other_line_number.txt
echo '**********'
echo 'TEST ERROR: Scoring task 5, where the provided list of line_numbers does not contain all lines from the gold file.'
python3 task5.py --gold_file_path=${gold_file_task5} --pred_file_path=${scorer_tests_path}task5_not_all_lines.txt
echo '**********'