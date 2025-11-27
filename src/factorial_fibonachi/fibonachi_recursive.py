from benchmarks.benchmark import benchmark


@benchmark
def fibonachi_recursive(number: int) -> int:
    """
    Вычисляет число Фибоначчи рекурсивным методом.

    Args:
        number: Порядковый номер числа(неотрицательное число)
            в последовательности Фибоначчи.

    Returns:
        Число Фибоначчи.
    """
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonachi_recursive(number - 1) + fibonachi_recursive(number - 2)
