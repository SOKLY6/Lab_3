from benchmarks.benchmark import benchmark


@benchmark
def counting_sort(lst: list[int]) -> list[int]:
    """
    Сортирует список методом сортировки подсчётом.

    Args:
        lst: Список целых чисел для сортировки.

    Returns:
        Отсортированный список.
    """
    if len(lst) <= 1:
        return lst
    max_element = max(lst)
    min_element = min(lst)
    result_list = []
    if min_element >= 0:
        counting_list = [0 for i in range(max_element + 1)]
        for element in lst:
            counting_list[element] += 1
        for i in range(max_element + 1):
            result_list += [i] * counting_list[i]
    else:
        counting_list = [0 for i in range(max_element - min_element + 1)]
        for element in lst:
            counting_list[element + abs(min_element)] += 1
        for i in range(max_element - min_element + 1):
            result_list += [i + min_element] * counting_list[i]
    return result_list
