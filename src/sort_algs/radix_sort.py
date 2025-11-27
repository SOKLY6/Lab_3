from benchmarks.benchmark import benchmark

values = {
    '': 0,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
}


@benchmark
def radix_sort(lst: list[str], base: int | None = None) -> list[str]:
    """
    Сортирует список строк поразрядной сортировкой.

    Args:
        lst: Список строк для сортировки.
        base: Основание системы счисления (до 36).

    Returns:
        Отсортированный список.
    """
    if len(lst) <= 1:
        return lst
    if not base:
        base = 10
    if base > 36:
        raise ValueError('base must be 36 or less')
    if base > 10:
        lst = [number.upper() for number in lst]
    iterations = max([len(x) for x in lst])
    for i in range(iterations - 1, -1, -1):
        iteration_list: list[list[str]] = [[] for _ in range(base)]
        for element in lst:
            iteration_list[values[element[i : i + 1]] % base].append(element)
        lst = [
            element
            for list_index in range(base)
            for element in iteration_list[list_index]
        ]
    return lst
