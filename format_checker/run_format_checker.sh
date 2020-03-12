#!/usr/bin/env bash
PROJ_DIR="$(dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))"
format_checker_tests_path=${PROJ_DIR}'/format_checker/data/'

echo '======= Task 5 OK: Running the format checker with correct output.'
python3 task5.py --pred_file_path=${format_checker_tests_path}task5_OK.txt
echo '======='
echo '======= Task 5 NOT OK: Running the format checker with some missing line_numbers.'
python3 task5.py --pred_file_path=${format_checker_tests_path}task5_NOTOK_MISSING_ID.txt
echo '======='
echo '======= Task 5 NOT OK: Running the format checker where the provided list of line_numbers contains duplicates.'
python3 task5.py --pred_file_path=${format_checker_tests_path}'task5_NOTOK_DUP_LINE_NUM.txt'
echo '======='
echo '======= Task 5 NOT OK: Running the format checker where the line_numbers start from 0'
python3 task5.py --pred_file_path=${format_checker_tests_path}'task5_NOTOK_0.txt'
echo '======='