from typing import Any, Callable

from benchmarks.benchmark import benchmark


def heapify(
    lst: list[int],
    len_lst: int,
    i: int,
    key: Callable[[int], Any],
    cmp: Callable[[int, int], int],
) -> None:
    """
    Преобразует поддерево с корнем i в max-heap.

    Args:
        lst: Список для преобразования.
        len_lst: Размер heap.
        i: Индекс корня поддерева.
        key: Функция для извлечения ключа сравнения.
        cmp: Функция сравнения, возвращает 1 если первый элемент меньше.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len_lst and cmp(key(lst[largest]), key(lst[left])) == 1:
        largest = left
    if right < len_lst and cmp(key(lst[largest]), key(lst[right])) == 1:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, len_lst, largest, key, cmp)


@benchmark
def heap_sort(
    lst: list[int],
    key: Callable[[int], Any] | None = None,
    cmp: Callable[[int, int], int] | str | None = None,
) -> list[int]:
    """
    Сортирует список методом пирамидальной сортировки.

    Args:
        lst: Список целых чисел для сортировки.
        key: Функция для извлечения ключа сравнения.
        cmp: Функция сравнения элементов.

    Returns:
        Отсортированный список.
    """
    len_lst = len(lst)
    if len_lst <= 1:
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

    for i in range(len_lst // 2, -1, -1):
        heapify(lst, len_lst, i, key, cmp)
    for i in range(len_lst - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0, key, cmp)
    return lst
