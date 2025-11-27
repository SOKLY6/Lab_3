from benchmarks.benchmark import benchmark


@benchmark
def factorial_default(number: int) -> int:
    """
    Вычисляет факториал числа итеративным методом.

    Args:
        number: Неотрицательное число для вычисления факториала.

    Returns:
        Факториал числа.
    """
    factorial = 1
    for n in range(1, number + 1):
        factorial *= n
    return factorial
