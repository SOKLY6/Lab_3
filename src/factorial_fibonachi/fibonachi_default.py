from benchmarks.benchmark import benchmark


@benchmark
def fibonachi_default(number: int) -> int:
    """
    Вычисляет число Фибоначчи итеративным методом.

    Args:
        number: Порядковый номер числа(неотрицательное число)
            в последовательности Фибоначчи.

    Returns:
        Число Фибоначчи.
    """
    if number == 0:
        return 0
    if number == 2 or number == 1:
        return 1
    fib1 = 1
    fib2 = 1
    for _i in range(3, number + 1):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    return fib2
