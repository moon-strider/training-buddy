import os
import pytest
import numpy as np

from utilities.utilities import *
from utilities.calc import VO2max, calories
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


def test_calories():
    assert calories(1, 95, 189, 21, 'moderate') == 3150
    assert calories(0, 80, 175, 29, 'light') == 2185


def test_VO2max():
    assert VO2max(21, 45) == 66
    assert VO2max(29, 65) == 44


def test_ensure_non_negative():
    for _ in range(10):
        arr = [np.random.randint(-1000, 1000) for _ in range(100)]
        arr[49] = -abs(arr[49])
        with pytest.raises(ValueError):
            ensure_non_negative(*arr)

        arr = np.abs(arr)
        ensure_non_negative(*arr)
        

def test_ensure_date_correctness():
    for _ in range(10):
        dd_c = str(np.random.randint(1, 28))
        mm_c = str(np.random.randint(1, 12))
        yyyy_c = str(np.random.randint(0, 2020))
        ensure_date_correctness(f"{dd_c}.{mm_c}.{yyyy_c}")
        with pytest.raises(ValueError):
            dd_e = str(np.random.randint(32, 40))
            ensure_date_correctness(f"{dd_e}.{mm_c}.{yyyy_c}")
        with pytest.raises(ValueError):
            mm_e = str(np.random.randint(13, 40))
            ensure_date_correctness(f"{dd_c}.{mm_e}.{yyyy_c}")
        with pytest.raises(ValueError):
            yyyy_e = str(np.random.randint(-100, -1))
            ensure_date_correctness(f"{dd_c}.{mm_c}.{yyyy_e}")