ACTIVITY = {
    'none': 1.2,
    'light': 1.375,
    'moderate': 1.550,
    'very active': 1.725,
    'extreme': 1.9
}

DEFICIT = {
    'none': 1,
    'light': 0.95,
    'moderate': 0.9,
    'significant': 0.85,
    'extreme': 0.8
}


def VO2max(age: int, heart_rate: int) -> int:
    """
    Calculate VO2max value using resting heart rate and age.
    """
    return round(15 * (220 - age) / heart_rate)


def calories(male: bool, weight: float, height: float, age: int, activity: str, deficit='none') -> int:
    """
    Calculate recommended caloric intake using Mifflin-St Jeor formula.
    """
    return round((9.99 * weight + 6.25 * height - 4.92 * age + (5 if male else -161)) * ACTIVITY[activity] * DEFICIT[deficit])