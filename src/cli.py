import sys
from typing import Any

import typer

from factorial_fibonachi.factorial_default import factorial_default
from factorial_fibonachi.factorial_recursive import factorial_recursive
from factorial_fibonachi.fibonachi_default import fibonachi_default
from factorial_fibonachi.fibonachi_recursive import fibonachi_recursive
from sort_algs.bubble_sort import bubble_sort
from sort_algs.bucket_sort import bucket_sort
from sort_algs.counting_sort import counting_sort
from sort_algs.heap_sort import heap_sort
from sort_algs.quick_sort import quick_sort
from sort_algs.radix_sort import radix_sort
from structures.queue import Queue
from structures.stack import Stack
from test_cases.test_cases import (
    many_duplicates,
    nearly_sorted,
    rand_float_array,
    rand_int_array,
    reverse_sorted,
)

app = typer.Typer(help='CLI для работы с алгоритмами')

stack = Stack()
queue = Queue()


# FIBONACHI
fib_app = typer.Typer(help='Вычисление чисел Фибоначчи')
app.add_typer(fib_app, name='fibonachi')


@fib_app.command('default')
def fibonachi_default_cmd(n: int) -> None:
    """Вычисляет число Фибоначчи итеративным методом."""
    result = fibonachi_default(n)
    typer.echo(f'Fibonachi({n}) = {result}')


@fib_app.command('recursive')
def fibonachi_recursive_cmd(n: int) -> None:
    """Вычисляет число Фибоначчи рекурсивным методом."""
    result = fibonachi_recursive(n)
    typer.echo(f'Fibonachi({n}) = {result}')


# FACTORIAL
fact_app = typer.Typer(help='Вычисление факториала')
app.add_typer(fact_app, name='factorial')


@fact_app.command('default')
def factorial_default_cmd(n: int) -> None:
    """Вычисляет факториал итеративным методом."""
    result = factorial_default(n)
    typer.echo(f'{n}! = {result}')


@fact_app.command('recursive')
def factorial_recursive_cmd(n: int) -> None:
    """Вычисляет факториал рекурсивным методом."""
    result = factorial_recursive(n)
    typer.echo(f'{n}! = {result}')


# SORTS
sort_app = typer.Typer(help='Алгоритмы сортировки')
app.add_typer(sort_app, name='sort')


def print_array(arr: list[Any], max_display: int = 20) -> None:
    """Выводит массив, ограничивая количество элементов."""
    if len(arr) <= max_display:
        typer.echo(str(arr))
    else:
        typer.echo(f'{arr[:max_display]}... (всего {len(arr)} элементов)')


@sort_app.command('bubble')
def sort_bubble(
    test_type: str,
    n: int | None = None,
    low: int | None = None,
    high: int | None = None,
    distinct: bool = False,
    seed: int | None = None,
    k_unique: int = 5,
    swaps: int = 5,
    custom: str | None = None,
) -> None:
    """Сортировка пузырьком."""
    arr = generate_test_array(
        test_type, n, low, high, distinct, seed, k_unique, swaps, custom
    )
    if arr:
        typer.echo('Исходный массив: ', nl=False)
        print_array(arr)
        result = bubble_sort(arr.copy())
        typer.echo('Отсортированный: ', nl=False)
        print_array(result)


@sort_app.command('quick')
def sort_quick(
    test_type: str,
    n: int | None = None,
    low: int | None = None,
    high: int | None = None,
    distinct: bool = False,
    seed: int | None = None,
    k_unique: int = 5,
    swaps: int = 5,
    custom: str | None = None,
) -> None:
    """Быстрая сортировка."""
    arr = generate_test_array(
        test_type, n, low, high, distinct, seed, k_unique, swaps, custom
    )
    if arr:
        typer.echo('Исходный массив: ', nl=False)
        print_array(arr)
        result = quick_sort(arr.copy())
        typer.echo('Отсортированный: ', nl=False)
        print_array(result)


@sort_app.command('heap')
def sort_heap(
    test_type: str,
    n: int | None = None,
    low: int | None = None,
    high: int | None = None,
    distinct: bool = False,
    seed: int | None = None,
    k_unique: int = 5,
    swaps: int = 5,
    custom: str | None = None,
) -> None:
    """Пирамидальная сортировка."""
    arr = generate_test_array(
        test_type, n, low, high, distinct, seed, k_unique, swaps, custom
    )
    if arr:
        typer.echo('Исходный массив: ', nl=False)
        print_array(arr)
        result = heap_sort(arr.copy())
        typer.echo('Отсортированный: ', nl=False)
        print_array(result)


@sort_app.command('counting')
def sort_counting(
    test_type: str,
    n: int | None = None,
    low: int | None = None,
    high: int | None = None,
    distinct: bool = False,
    seed: int | None = None,
    k_unique: int = 5,
    swaps: int = 5,
    custom: str | None = None,
) -> None:
    """Сортировка подсчётом."""
    arr = generate_test_array(
        test_type, n, low, high, distinct, seed, k_unique, swaps, custom
    )
    if arr:
        typer.echo('Исходный массив: ', nl=False)
        print_array(arr)
        result = counting_sort(arr.copy())
        typer.echo('Отсортированный: ', nl=False)
        print_array(result)


@sort_app.command('bucket')
def sort_bucket(
    test_type: str,
    n: int | None = None,
    low: float | None = None,
    high: float | None = None,
    seed: int | None = None,
    custom: str | None = None,
) -> None:
    """Блочная сортировка (для вещественных чисел)."""
    if test_type == 'rand_float':
        arr = rand_float_array(n, low or 0.0, high or 1.0, seed)
    elif test_type == 'custom' and custom:
        arr = [float(x.strip()) for x in custom.split(',')]
    else:
        typer.echo('Для bucket используйте rand_float или custom')
        return

    typer.echo('Исходный массив: ', nl=False)
    print_array(arr)
    result = bucket_sort(arr.copy())
    typer.echo('Отсортированный: ', nl=False)
    print_array(result)


@sort_app.command('radix')
def sort_radix(
    test_type: str,
    n: int | None = None,
    base: int = 10,
    custom: str | None = None,
) -> None:
    """Поразрядная сортировка (для строк)."""
    if test_type == 'custom' and custom:
        arr = [x.strip() for x in custom.split(',')]
    else:
        typer.echo('Для radix используйте custom с строками')
        return

    typer.echo(f'Исходный массив: {arr}')
    result = radix_sort(arr.copy(), base)
    typer.echo(f'Отсортированный: {result}')


def generate_test_array(
    test_type, n, low, high, distinct, seed, k_unique, swaps, custom
) -> None | list[Any]:
    """Генерирует тестовый массив."""
    try:
        if test_type == 'rand_int':
            return rand_int_array(n, low, high, distinct, seed)
        elif test_type == 'rand_float':
            return rand_float_array(n, low or 0.0, high or 1.0, seed)
        elif test_type == 'reverse_sorted':
            return reverse_sorted(n, low or -100, high or 100)
        elif test_type == 'many_duplicates':
            return many_duplicates(n, k_unique, seed)
        elif test_type == 'nearly_sorted':
            return nearly_sorted(n, swaps, seed)
        elif test_type == 'custom' and custom:
            return [int(x.strip()) for x in custom.split(',')]
        else:
            typer.echo(f'Неизвестный тип test_case: {test_type}')
            return None
    except Exception as e:
        typer.echo(f'Ошибка генерации массива: {e}', err=True)
        return None


# STACK
stack_app = typer.Typer(help='Операции со стеком')
app.add_typer(stack_app, name='stack')


@stack_app.command('push')
def stack_push(value: int) -> None:
    """Добавить элемент в стек."""
    stack.push(value)
    typer.echo(f'Добавлено: {value}')


@stack_app.command('pop')
def stack_pop() -> None:
    """Удалить элемент из стека."""
    try:
        value = stack.pop()
        typer.echo(f'Удалено: {value}')
    except ValueError as e:
        typer.echo(f'Ошибка: {e}', err=True)


@stack_app.command('peek')
def stack_peek() -> None:
    """Посмотреть верхний элемент."""
    try:
        typer.echo(f'Верхний элемент: {stack.peek()}')
    except ValueError as e:
        typer.echo(f'Ошибка: {e}', err=True)


@stack_app.command('min')
def stack_min() -> None:
    """Получить минимальный элемент."""
    try:
        typer.echo(f'Минимум: {stack.min()}')
    except ValueError as e:
        typer.echo(f'Ошибка: {e}', err=True)


@stack_app.command('length')
def stack_length() -> None:
    """Размер стека."""
    typer.echo(f'Размер: {len(stack)}')


@stack_app.command('is-empty')
def stack_is_empty() -> None:
    """Проверить, пуст ли стек."""
    typer.echo(f'Пуст: {stack.is_empty()}')


# QUEUE
queue_app = typer.Typer(help='Операции с очередью')
app.add_typer(queue_app, name='queue')


@queue_app.command('enqueue')
def queue_enqueue(value: int) -> None:
    """Добавить элемент в очередь."""
    queue.enqueue(value)
    typer.echo(f'Добавлено: {value}')


@queue_app.command('dequeue')
def queue_dequeue() -> None:
    """Удалить элемент из очереди."""
    try:
        value = queue.dequeue()
        typer.echo(f'Удалено: {value}')
    except ValueError as e:
        typer.echo(f'Ошибка: {e}', err=True)


@queue_app.command('front')
def queue_front() -> None:
    """Посмотреть первый элемент."""
    try:
        typer.echo(f'Первый элемент: {queue.front()}')
    except ValueError as e:
        typer.echo(f'Ошибка: {e}', err=True)


@queue_app.command('length')
def queue_length() -> None:
    """Размер очереди."""
    typer.echo(f'Размер: {len(queue)}')


@queue_app.command('is-empty')
def queue_is_empty() -> None:
    """Проверить, пуста ли очередь."""
    typer.echo(f'Пуста: {queue.is_empty()}')


# INTERACTIVE
def interactive_mode() -> None:
    """Запускает интерактивный режим для построчного ввода команд."""
    typer.echo('=== CLI для работы с алгоритмами ===')
    typer.echo(
        'Вводите команды построчно.',
        " Введите 'exit' или нажмите Ctrl+D для выхода.",
    )
    typer.echo("Введите 'help' для справки.")
    typer.echo()

    try:
        for line in sys.stdin:
            line = line.strip()

            if not line:
                continue

            if line.lower() in ['exit', 'quit']:
                typer.echo('Выход из программы.')
                break

            if line.lower() == 'help':
                typer.echo("""
Доступные команды:
  fibonachi default <n>              - Вычислить число Фибоначчи итеративно
  fibonachi recursive <n>            - Вычислить число Фибоначчи рекурсивно
  factorial default <n>              - Вычислить факториал итеративно
  factorial recursive <n>            - Вычислить факториал рекурсивно
  
  sort <algorithm> <test_type> [options]
    algorithm: bubble, quick, heap, counting, bucket, radix
    test_type: rand_int, rand_float, reverse_sorted, 
                           many_duplicates, nearly_sorted, custom 
    
  stack push <value>                 - Добавить в стек
  stack pop                          - Удалить из стека
  stack peek                         - Посмотреть верхний элемент
  stack min                          - Минимальный элемент
  stack length                       - Размер стека
  stack is-empty                     - Проверить, пуст ли стек
  
  queue enqueue <value>              - Добавить в очередь
  queue dequeue                      - Удалить из очереди
  queue front                        - Посмотреть первый элемент
  queue length                       - Размер очереди
  queue is-empty                     - Проверить, пуста ли очередь
  
  exit / quit                        - Выход
  help                               - Эта справка
                """)
                continue

            old_argv = sys.argv
            try:
                sys.argv = ['cli'] + line.split()
                app(standalone_mode=False)
            except SystemExit:
                pass
            except Exception as e:
                typer.echo(f'Ошибка: {e}', err=True)
            finally:
                sys.argv = old_argv

    except (KeyboardInterrupt, EOFError):
        typer.echo('\nВыход из программы.')


def cli() -> None:
    """Главная функция CLI."""
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        app()
