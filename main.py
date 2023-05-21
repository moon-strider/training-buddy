import json
import os
import logging
import numpy as np


# TODO: init dirs


MEALS_FP = 'data/meals.json'


logging.basicConfig(
    filename='debug.log', 
    encoding='utf-8', 
    level=logging.DEBUG, 
    format='%(asctime)s %(levelname)-8s %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)


def input_meal(date: str, calories: float, proteins: float, fats: float, carbs: float, is_healthy: bool) -> None:
    (dd, mm, yyyy) = date.split('.')

    if len(dd) != 2 or len(mm) != 2 or len(yyyy) != 4:
        raise ValueError('The date must be in \"dd.mm.yyyy\" format.')

    if not os.path.exists(MEALS_FP):
        logging.debug(f'file not found at \"{MEALS_FP}\", creating the file...')
        tmp = open(MEALS_FP, 'w', encoding='utf-8')
        json_object = json.dumps({date: {}}, ensure_ascii=False, indent=4)
        tmp.write(json_object)
        tmp.close()
        logging.debug(f'file created at \"{MEALS_FP}\"')

    datafile = open(MEALS_FP, 'r', encoding='utf-8')
    data: dict = json.load(datafile)
    datafile.close()
    logging.debug(f'json file loaded and decoded successfully at \"{MEALS_FP}\"')

    with open(MEALS_FP, 'w', encoding='utf-8') as file:    
        # TODO: check validity of the date

        payload = {
            'calories': calories,
            'proteins': proteins,
            'fats': fats,
            'carbs': carbs,
            'is_healthy': is_healthy
        }

        index = 1

        if date in data.keys():
            try:
                index = int(list(data[date].keys())[-1]) + 1
            except IndexError:
                pass
        else:
            data[date] = {}

        data[date][index] = payload
        logging.debug(f'appending to {date} on index {index}')

        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    input_meal('11.11.2001', 150, 150, 200, 150, False)
    input_meal('11.11.2001', 150, 150, 200, 170, False)
    input_meal('11.12.2001', 150, 150, 200, 190, False)
    #input_meal('111.11.2001', 150, 150, 200, 150, False)