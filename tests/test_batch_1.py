import json
import os

from utils.utils import input_meal


MEALS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meals.json')


def test_input_meal():
    input_meal('11.11.2001', 150, 150, 200, 150, False, MEALS_FP=MEALS_FP)
    input_meal('11.11.2001', 150, 150, 200, 170, False, MEALS_FP=MEALS_FP)
    input_meal('11.12.2001', 150, 150, 200, 190, False, MEALS_FP=MEALS_FP)

    assert os.path.exists(MEALS_FP)

    file = open(MEALS_FP, 'r')

    assert json.load(file) == \
    {
        "11.11.2001": {
            "1": {
                "calories": 150,
                "proteins": 150,
                "fats": 200,
                "carbs": 150,
                "is_healthy": False
            },
            "2": {
                "calories": 150,
                "proteins": 150,
                "fats": 200,
                "carbs": 170,
                "is_healthy": False
            }
        },
        "11.12.2001": {
            "1": {
                "calories": 150,
                "proteins": 150,
                "fats": 200,
                "carbs": 190,
                "is_healthy": False
            }
        }
    }
    file.close()

    os.remove(MEALS_FP)