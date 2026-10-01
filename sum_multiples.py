def calculate_sum_multiples_of_5(start: int = 500, end: int = 1000) -> int:
    """
    Обчислює суму натуральних чисел, кратних 5, у діапазоні від start до end.
    """
    total_sum = 0
    for num in range(start, end + 1):
        if num % 5 == 0:
            total_sum += num
    return total_sum