from typing import Any, Callable

from benchmarks.benchmark import benchmark


@benchmark
def bubble_sort(
    lst: list[int],
    key: Callable[[int], Any] | str | None = None,
    cmp: Callable[[int, int], int] | str | None = None,
) -> list[int]:
    """
    Сортирует список методом сортировки выбором.

    Args:
        lst: Список целых чисел для сортировки.
        key: Функция для извлечения ключа сравнения.
        cmp: Функция сравнения элементов.

    Returns:
        Отсортированный список.
    """
    if len(lst) <= 1:
        return lst
    if not key:

        def key(x: int) -> int:
            return x
    elif key == 'abs':

        def key(x: int) -> int:
            return abs(x)
    elif key == 'mod 10':

        def key(x: int) -> int:
            return x % 10

    if not cmp:

        def cmp(x: Any, y: Any) -> int:
            if x < y:
                return 1
            if x == y:
                return 0
            return -1
    elif cmp == 'reverse':

        def cmp(x: Any, y: Any) -> int:
            if x > y:
                return 1
            if x == y:
                return 0
            return -1

    for i in range(len(lst) - 1):
        index_min_element = i
        for j in range(i + 1, len(lst)):
            if cmp(key(lst[j]), key(lst[index_min_element])) == 1:
                index_min_element = j
        if index_min_element != i:
            lst[i], lst[index_min_element] = lst[index_min_element], lst[i]
    return lst
