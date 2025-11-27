import functools
import time
from typing import Any, Callable


def benchmark(function: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции.

    Args:
        function: Функция, время выполнения которой нужно измерить.

    Returns:
        Обёрнутая функция с измерением времени выполнения.
    """

    @functools.wraps(function)
    def wrapper(*args: Any, **kwards: Any) -> Any:
        time_start = time.perf_counter()
        result = function(*args, **kwards)
        time_end = time.perf_counter()
        time_result = time_end - time_start
        print(
            f'Выполнение команды {function.__name__}',
            f' заняло: {time_result * 1000:.3f}мс',
        )
        return result

    return wrapper
