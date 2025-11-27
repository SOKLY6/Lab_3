from typing import Any, Callable

from benchmarks.benchmark import benchmark


@benchmark
def quick_sort(
    lst: list[int],
    key: Callable[[int], Any] | None = None,
    cmp: Callable[[int, int], int] | str | None = None,
) -> list[int]:
    """
    Сортирует список методом быстрой сортировки.

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

    basic_element = lst.pop()
    lst_left = []
    lst_right = []
    for element in lst:
        if cmp(key(element), key(basic_element)) == 1:
            lst_left.append(element)
        else:
            lst_right.append(element)
    return (
        quick_sort(lst_left, key, cmp)
        + [basic_element]
        + quick_sort(lst_right, key, cmp)
    )
