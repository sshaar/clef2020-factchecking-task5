from unittest import TestCase
from os.path import dirname, join

from scorer import task5

_ROOT_DIR = dirname(dirname(__file__))
_GOLD_FILE_1 = join(_ROOT_DIR, 'data/task5/English/Task5-English-1st-Presidential.txt')
_PRED_FILE_1 = join(_ROOT_DIR, 'scorer/data/task5_random_baseline.txt')
_PRED_FILE_1_NOTFULL = join(_ROOT_DIR, 'scorer/data/task5_not_all_lines.txt')


class ScorerTask5(TestCase):
    def test_average_precision(self):
        y_gold_labels = {1: 0, 2: 1, 3: 0, 4: 0, 5: 1}
        y_pred_ranked = [1, 2, 3, 4, 5]
        num_relevant = 2
        avg_p = task5._compute_average_precision(y_gold_labels, y_pred_ranked)
        self.assertEqual(avg_p, (0.5+0.4)/num_relevant)

        y_gold_labels = {1: 1, 2: 0, 3: 1, 4: 0, 5: 1}
        y_pred_ranked = [1, 2, 3, 4, 5]
        num_relevant = 3
        avg_p = task5._compute_average_precision(y_gold_labels, y_pred_ranked)
        self.assertEqual(avg_p, (1 + 2/3 + 3/5)/num_relevant)

        y_gold_labels = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        y_pred_ranked = [1, 2, 3, 4, 5]
        avg_p = task5._compute_average_precision(y_gold_labels, y_pred_ranked)
        self.assertEqual(avg_p, 0)

    def test_precisions(self):
        y_gold_labels = {1: 1, 2: 0, 3: 1, 4: 0, 5: 1}
        y_pred_ranked = [1, 2, 3, 4, 5]
        prec = task5._compute_precisions(y_gold_labels, y_pred_ranked, len(y_pred_ranked))
        self.assertEqual(prec, [1, 0.5, 2/3, 2/4, 3/5])

        y_gold_labels = {1: 0, 2: 0}
        y_pred_ranked = [1, 2]
        prec = task5._compute_precisions(y_gold_labels, y_pred_ranked, len(y_pred_ranked))
        self.assertEqual(prec, [0, 0])

    def test_reciprocal_rank(self):
        y_gold_labels = {1: 1, 2: 0, 3: 1, 4: 0, 5: 1}

        rr = task5._compute_reciprocal_rank(y_gold_labels, [1, 2, 3, 4, 5])
        self.assertEqual(rr, 1)
        rr = task5._compute_reciprocal_rank(y_gold_labels, [5, 4, 3, 2, 1])
        self.assertEqual(rr, 1)
        rr = task5._compute_reciprocal_rank(y_gold_labels, [2, 4, 1, 3, 5])
        self.assertEqual(rr, 1/3)
        rr = task5._compute_reciprocal_rank(y_gold_labels, [2, 5, 4, 1, 3])
        self.assertEqual(rr, 1/2)

    def test_read_gold_and_pred(self):
        gold_labels, pred_ranked = task5._read_gold_and_pred(_GOLD_FILE_1, _PRED_FILE_1)

        self.assertEqual(list(gold_labels.keys()), [p[0] for p in pred_ranked])
        self.assertGreater(len([k for k, v in gold_labels.items() if v == 1]), 20)
        self.assertGreater(len([k for k, v in gold_labels.items() if v == 0]), 1000)

        with self.assertRaises(ValueError):
          task5._read_gold_and_pred(_GOLD_FILE_1, _PRED_FILE_1_NOTFULL)
