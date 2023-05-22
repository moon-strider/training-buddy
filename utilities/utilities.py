import json
import os
import logging
import datetime


PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

DATA_DIR = os.path.join(PROJECT_PATH, 'data')

MEALS_FP = os.path.join(DATA_DIR, 'meals.json')
STATS_FP = os.path.join(DATA_DIR, 'stats.json')

DIR_LIST = [DATA_DIR]
FILE_LIST = [MEALS_FP, STATS_FP]


logging.basicConfig(
    filename='debug.log', 
    encoding='utf-8', 
    level=logging.DEBUG, 
    format='%(asctime)s %(levelname)-8s %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

print(STATS_FP)


def ensure_date_correctness(date: str) -> None:
    (dd, mm, yyyy) = date.split('.')

    try:
        _ = datetime.datetime(int(yyyy), int(mm), int(dd))
    except ValueError:
        raise ValueError("The provided date is not correct.")

    if len(dd) != 2 or len(mm) != 2 or len(yyyy) != 4:
        raise ValueError('The date must be in \"dd.mm.yyyy\" format.')


def ensure_non_negative(*vars) -> None:
    for var in vars:
        if var < 0:
            raise ValueError("One of the provided arguments may not be negative.")
        

def ensure_file_exists(FP: str) -> None:
    if not os.path.exists(FP):
        logging.debug(f'file not found at \"{FP}\", creating the file...')
        tmp = open(FP, 'w', encoding='utf-8')
        json_object = json.dumps({}, ensure_ascii=False, indent=4)
        tmp.write(json_object)
        tmp.close()
        logging.debug(f'file created at \"{FP}\"')


def retrieve_json(FP: str) -> dict:
    logging.debug(f'trying to load and decode json at \"{FP}\"')
    datafile = open(FP, 'r', encoding='utf-8')
    data: dict = json.load(datafile)
    datafile.close()
    logging.debug(f'json file loaded and decoded successfully at \"{FP}\"')
    return data


def input_meal(date: str, calories: float, proteins: float, fats: float, carbs: float, is_healthy: bool, meals_fp=MEALS_FP) -> None:
    ensure_date_correctness(date)
    ensure_non_negative(calories, proteins, fats, carbs)
    ensure_file_exists(meals_fp)

    data = retrieve_json(meals_fp)

    payload = {
        'calories': calories,
        'proteins': proteins,
        'fats': fats,
        'carbs': carbs,
        'is_healthy': is_healthy
    }

    with open(meals_fp, 'w', encoding='utf-8') as file:    
        index = 1

        if date in data.keys():
            try:
                index = int(list(data[date].keys())[-1]) + 1
            except IndexError:
                pass
        else:
            data[date] = {}

        data[date][index] = payload
        logging.debug(f'appending meal to {date} on index {index}')

        json.dump(data, file, ensure_ascii=False, indent=4)


def input_stats(date: str, weight: float, heart_rate: int, steps: int, age: int, stats_fp=STATS_FP) -> None:
    ensure_date_correctness(date)
    ensure_non_negative(weight, heart_rate, steps, age)
    ensure_file_exists(stats_fp)

    data = retrieve_json(stats_fp)

    payload = {
        'weight': weight,
        'heart_rate': heart_rate,
        'steps': steps,
        'VO2max': 15 * (220 - age) / heart_rate
    }

    with open(stats_fp, 'w', encoding='utf-8') as file:    
        if date in data.keys():
            raise ValueError("Such a date already has data associated with it.")
        else:
            data[date] = payload

        logging.debug(f'appending stats to {date}')

        json.dump(data, file, ensure_ascii=False, indent=4)


def init_dirs_and_files() -> None:
    for dir in DIR_LIST:
        if not os.path.exists(dir):
            os.makedirs(dir)
    
    for file in FILE_LIST:
        if not os.path.exists(file):
            tmp = open(file, 'w')
            tmp.close()