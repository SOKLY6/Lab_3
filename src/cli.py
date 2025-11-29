import sys
from typing import Any, Annotated
import shlex

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
    n: Annotated[int | None, typer.Argument()] = None,
    low: Annotated[int | None, typer.Argument()] = None,
    high: Annotated[int | None, typer.Argument()] = None,
    distinct: Annotated[bool, typer.Option('--distinct')] = False,
    seed: Annotated[int | None, typer.Option('--seed')] = None,
    k_unique: Annotated[int, typer.Option('--k-unique')] = 5,
    swaps: Annotated[int, typer.Option('--swaps')] = 5,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Сортировка пузырьком.
    
    Примеры:
        sort bubble rand_int 20 1 100
        sort bubble rand_int 15 -50 50 --distinct --seed 42
        sort bubble custom --custom "5,2,8,1,9"
    """
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
    n: Annotated[int | None, typer.Argument()] = None,
    low: Annotated[int | None, typer.Argument()] = None,
    high: Annotated[int | None, typer.Argument()] = None,
    distinct: Annotated[bool, typer.Option('--distinct')] = False,
    seed: Annotated[int | None, typer.Option('--seed')] = None,
    k_unique: Annotated[int, typer.Option('--k-unique')] = 5,
    swaps: Annotated[int, typer.Option('--swaps')] = 5,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Быстрая сортировка.
    
    Примеры:
        sort quick rand_int 20 1 100
        sort quick nearly_sorted 30 --swaps 5 --seed 42
    """
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
    n: Annotated[int | None, typer.Argument()] = None,
    low: Annotated[int | None, typer.Argument()] = None,
    high: Annotated[int | None, typer.Argument()] = None,
    distinct: Annotated[bool, typer.Option('--distinct')] = False,
    seed: Annotated[int | None, typer.Option('--seed')] = None,
    k_unique: Annotated[int, typer.Option('--k-unique')] = 5,
    swaps: Annotated[int, typer.Option('--swaps')] = 5,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Пирамидальная сортировка.
    
    Примеры:
        sort heap rand_int 20 1 100
        sort heap reverse_sorted 25 -100 100
    """
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
    n: Annotated[int | None, typer.Argument()] = None,
    low: Annotated[int | None, typer.Argument()] = None,
    high: Annotated[int | None, typer.Argument()] = None,
    distinct: Annotated[bool, typer.Option('--distinct')] = False,
    seed: Annotated[int | None, typer.Option('--seed')] = None,
    k_unique: Annotated[int, typer.Option('--k-unique')] = 5,
    swaps: Annotated[int, typer.Option('--swaps')] = 5,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Сортировка подсчётом.
    
    Примеры:
        sort counting rand_int 50 1 100
        sort counting many_duplicates 50 --k-unique 5
    """
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
    n: Annotated[int | None, typer.Argument()] = None,
    low: Annotated[float | None, typer.Argument()] = None,
    high: Annotated[float | None, typer.Argument()] = None,
    seed: Annotated[int | None, typer.Option('--seed')] = None,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Блочная сортировка (для вещественных чисел).
    
    Примеры:
        sort bucket rand_float 30 0.0 1.0
        sort bucket rand_float 30 0.0 1.0 --seed 42
        sort bucket custom --custom "1.5,2.3,0.8"
    """
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
    base: Annotated[int, typer.Option('--base')] = 10,
    custom: Annotated[str | None, typer.Option('--custom')] = None,
) -> None:
    """
    Поразрядная сортировка (для строк).
    
    Примеры:
        sort radix custom --custom "123,45,789"
        sort radix custom --custom "ABC,ZZ,AAA" --base 36
    """
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
    value = stack.pop()
    typer.echo(f'Удалено: {value}')


@stack_app.command('peek')
def stack_peek() -> None:
    """Посмотреть верхний элемент."""
    typer.echo(f'Верхний элемент: {stack.peek()}')


@stack_app.command('min')
def stack_min() -> None:
    """Получить минимальный элемент."""
    typer.echo(f'Минимум: {stack.min()}')


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
    value = queue.dequeue()
    typer.echo(f'Удалено: {value}')


@queue_app.command('front')
def queue_front() -> None:
    """Посмотреть первый элемент."""
    typer.echo(f'Первый элемент: {queue.front()}')


@queue_app.command('length')
def queue_length() -> None:
    """Размер очереди."""
    typer.echo(f'Размер: {len(queue)}')


@queue_app.command('is-empty')
def queue_is_empty() -> None:
    """Проверить, пуста ли очередь."""
    typer.echo(f'Пуста: {queue.is_empty()}')


def show_help() -> None:
    """Показывает справку по командам."""
    typer.echo("""
Доступные команды:

=== Математические функции ===
  fibonachi default <n>              - Число Фибоначчи итеративно
  fibonachi recursive <n>            - Число Фибоначчи рекурсивно
  factorial default <n>              - Факториал итеративно
  factorial recursive <n>            - Факториал рекурсивно

=== Сортировка ===
  sort <algorithm> <test_type> [аргументы] [опции]
  
  Алгоритмы: bubble, quick, heap, counting, bucket, radix
  
  Типы тестовых данных:
  
  1. rand_int <n> <low> <high> [--distinct] [--seed <число>]
     Примеры:
       sort quick rand_int 20 1 100
       sort bubble rand_int 15 -50 50 --distinct --seed 42
  
  2. rand_float <n> <low> <high> [--seed <число>] (только bucket)
     Пример:
       sort bucket rand_float 30 0.0 1.0 --seed 42
  
  3. reverse_sorted <n> [<low> <high>]
     Примеры:
       sort heap reverse_sorted 25
       sort heap reverse_sorted 25 -100 100
  
  4. many_duplicates <n> [--k-unique <число>] [--seed <число>]
     Примеры:
       sort counting many_duplicates 50
       sort counting many_duplicates 50 --k-unique 10 --seed 42
  
  5. nearly_sorted <n> [--swaps <число>] [--seed <число>]
     Примеры:
       sort quick nearly_sorted 30
       sort quick nearly_sorted 30 --swaps 5 --seed 42
  
  6. custom --custom "элементы,через,запятую"
     Примеры:
       sort bubble custom --custom "5,2,8,1,9"
       sort radix custom --custom "123,45,789" --base 10

=== Стек ===
  stack push <value>      - Добавить элемент
  stack pop               - Удалить элемент
  stack peek              - Показать верхний элемент
  stack min               - Минимальный элемент
  stack length            - Размер стека
  stack is-empty          - Проверить пустоту

=== Очередь ===
  queue enqueue <value>   - Добавить элемент
  queue dequeue           - Удалить элемент
  queue front             - Показать первый элемент
  queue length            - Размер очереди
  queue is-empty          - Проверить пустоту

=== Управление ===
  exit / quit             - Выход
  help                    - Эта справка
    """)


def cli() -> None:
    """Главная функция CLI."""
    app()
