import math

def calculate_y(a: float, b: float, x: float, y_in: float) -> float:
    """
    Обчислює значення виразу: y = (|a - b| + cos(x)) / (1 + sqrt(y_in))
    """
    denominator = 1 + math.sqrt(y_in)
    if denominator == 0:
        raise ValueError("Знаменник не може дорівнювати 0!")
    
    numerator = abs(a - b) + math.cos(x)
    return numerator / denominator