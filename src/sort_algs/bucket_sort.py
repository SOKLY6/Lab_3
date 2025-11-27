from benchmarks.benchmark import benchmark


def quick_sort_for_bucket_sort(
    lst: list[float],
) -> list[float]:
    """
    Вспомогательная быстрая сортировка для bucket_sort.

    Args:
        lst: Список вещественных чисел для сортировки.

    Returns:
        Отсортированный список.
    """
    if len(lst) <= 1:
        return lst
    basic_element = lst.pop()
    lst_left = []
    lst_right = []
    for element in lst:
        if element < basic_element:
            lst_left.append(element)
        else:
            lst_right.append(element)
    return (
        quick_sort_for_bucket_sort(lst_left)
        + [basic_element]
        + quick_sort_for_bucket_sort(lst_right)
    )


@benchmark
def bucket_sort(lst: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортирует список методом блочной сортировки.

    Args:
        lst: Список вещественных чисел для сортировки.
        buckets: Количество блоков.

    Returns:
        Отсортированный список.
    """
    if len(lst) <= 1:
        return lst
    max_element = max(lst)
    min_element = min(lst)
    if max_element == min_element:
        return lst
    if not buckets:
        buckets = len(lst)
    buckets_list: list[list[float]] = [[] for _ in range(buckets)]
    value_connection = {}
    normalized_list = []
    for number in lst:
        normalized_number = (number - min_element) / (
            max_element - min_element
        )
        value_connection[normalized_number] = number
        normalized_list.append(normalized_number)
    for normalized_number in normalized_list:
        index = int(normalized_number * buckets)
        if index == buckets:
            index = buckets - 1
        buckets_list[index].append(normalized_number)
    result_list = []
    for bucket in buckets_list:
        for normalized_number in quick_sort_for_bucket_sort(bucket):
            result_list.append(value_connection[normalized_number])
    return result_list
