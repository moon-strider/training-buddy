# TODO: divide test consts and other types

INPUT_MEAL_DICT = {
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

INPUT_STATS_DICT = {
    "11.11.2001": {
        "weight": 150,
        "heart_rate": 150,
        "steps": 200,
        "VO2max": 7.0
    },
    "12.11.2001": {
        "weight": 150,
        "heart_rate": 150,
        "steps": 200,
        "VO2max": 5.0
    }
}

# Countable exercises contain calories per rep, running, swimming, etc. contain calories per hour
EXERCISES = {
    'squats': 0.32,
    'push-ups': 0.3,
    'pull-ups': 1,
    'running': 1020,
    'swimming': 500
}