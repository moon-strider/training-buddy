import json
import os
import pytest

from utilities.utilities import input_meal, input_stats, retrieve_json
from .consts import INPUT_MEAL_DICT, INPUT_STATS_DICT


TESTS_PATH = os.path.dirname(os.path.abspath(__file__))

MEALS_FP_TEST = os.path.join(TESTS_PATH, 'meals.json')
STATS_FP_TEST = os.path.join(TESTS_PATH, 'stats.json')


# TODO: for meal and stats negative args = valueerror


def test_input_meal():
    input_meal('11.11.2001', 150, 150, 200, 150, False, meals_fp=MEALS_FP_TEST)
    input_meal('11.11.2001', 150, 150, 200, 170, False, meals_fp=MEALS_FP_TEST)
    input_meal('11.12.2001', 150, 150, 200, 190, False, meals_fp=MEALS_FP_TEST)

    with pytest.raises(ValueError):
        input_meal('111.12.2001', 150, 150, 200, 190, True, meals_fp=MEALS_FP_TEST)
    with pytest.raises(ValueError):
        input_meal('30.02.2000', 150, 150, 200, 190, True, meals_fp=MEALS_FP_TEST)

    assert os.path.exists(MEALS_FP_TEST)

    data = retrieve_json(MEALS_FP_TEST)

    assert data == INPUT_MEAL_DICT

    os.remove(MEALS_FP_TEST)


def test_input_stats():
    input_stats('11.11.2001', 150, 150, 200, 150, stats_fp=STATS_FP_TEST)
    input_stats('12.11.2001', 150, 150, 200, 170, stats_fp=STATS_FP_TEST)

    with pytest.raises(ValueError):
        input_stats('111.12.2001', 100, 150, 200, 57, stats_fp=STATS_FP_TEST)
    with pytest.raises(ValueError):
        input_stats('30.02.2000', 100, 150, 200, 57, stats_fp=STATS_FP_TEST)
    with pytest.raises(ValueError):
        input_stats('11.11.2001', 100, 150, 200, 57, stats_fp=STATS_FP_TEST)

    assert os.path.exists(STATS_FP_TEST)

    data = retrieve_json(STATS_FP_TEST)

    assert data == INPUT_STATS_DICT

    os.remove(STATS_FP_TEST)