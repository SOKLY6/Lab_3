import random

from sort_algs import heap_sort

def rand_int_array(n: int, low: int, high: int, distinct: bool = False, seed: int | None = None) -> list[int]:
    """
    Генерирует массив случайных целых чисел.

    Args:
        n: Размер массива.
        low: Нижняя граница диапазона.
        high: Верхняя граница диапазона.
        distinct: Если True, элементы будут уникальными.
        seed: Seed для генератора случайных чисел.

    Returns:
        Массив случайных целых чисел.
    """
    if seed is not None:
        random.seed(seed)
    if distinct:
        return random.sample(range(low, high), n)
    return [random.randint(low, high) for _i in range(n)]

def rand_float_array(n: int, low: float = 0.0, high: float = 1.0, seed: int | None = None) -> list[float]:
    """
    Генерирует массив случайных вещественных чисел.

    Args:
        n: Размер массива.
        low: Нижняя граница диапазона.
        high: Верхняя граница диапазона.
        seed: Seed для генератора случайных чисел.

    Returns:
        Массив случайных вещественных чисел.
    """
    if seed is not None:
        random.seed(seed)
    return [random.uniform(low, high) for _i in range(n)]

def reverse_sorted(n: int, low: int = -100, high: int = 100) -> list[int]:
    """
    Генерирует массив, отсортированный в обратном порядке.

    Args:
        n: Размер массива.
        low: Нижняя граница диапазона.
        high: Верхняя граница диапазона.

    Returns:
        Массив целых чисел, отсортированный по убыванию.
    """
    return heap_sort.heap_sort([random.randint(low, high) for _i in range(n)], cmp = lambda x, y: x > y)

def many_duplicates(n: int, k_unique: int = 5, seed: int | None = None) -> list[int]:
    """
    Генерирует массив с большим количеством повторяющихся элементов.

    Args:
        n: Размер массива.
        k_unique: Количество уникальных элементов.
        seed: Seed для генератора случайных чисел.

    Returns:
        Массив с повторяющимися элементами.
    """
    return rand_int_array(n, 1, k_unique+1, seed=seed)

def nearly_sorted(n: int, swaps: int = 5, seed: int | None = None) -> list[int]:
    """
    Генерирует почти отсортированный массив.

    Args:
        n: Размер массива.
        swaps: Количество случайных обменов элементов.
        seed: Seed для генератора случайных чисел.

    Returns:
        Почти отсортированный массив.
    """
    lst = heap_sort.heap_sort(rand_int_array(n, -100, 100, seed=seed))
    for _i in range(swaps):
        a, b = random.sample(range(0, n-1), 2)
        lst[a], lst[b] = lst[b], lst[a]
    return lst
