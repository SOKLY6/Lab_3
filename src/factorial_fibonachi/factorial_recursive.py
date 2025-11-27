from benchmarks.benchmark import benchmark


@benchmark
def factorial_recursive(number: int) -> int:
    """
    Вычисляет факториал числа рекурсивным методом.

    Args:
        number: Целое число для вычисления факториала.

    Returns:
        Факториал числа.
    """
    if number == 1 or number == 0:
        return 1
    return factorial_recursive(number - 1) * number
