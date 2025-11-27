import pytest
from src.structures.stack import Stack
from src.structures.queue import Queue


def test_stack_empty():
    """Тест создания пустого стека"""
    stack = Stack()
    assert stack.is_empty() == True
    assert len(stack) == 0


def test_stack_push():
    """Тест добавления элементов"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert len(stack) == 3
    assert stack.is_empty() == False


def test_stack_pop():
    """Тест удаления элементов (LIFO)"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() == True


def test_stack_peek():
    """Тест просмотра верхнего элемента без удаления"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2


def test_stack_min():
    """Тест отслеживания минимального элемента"""
    stack = Stack()
    stack.push(5)
    assert stack.min() == 5
    stack.push(3)
    assert stack.min() == 3
    stack.push(7)
    assert stack.min() == 3
    stack.push(1)
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 3


def test_stack_pop_empty():
    """Тест удаления из пустого стека (должна быть ошибка)"""
    stack = Stack()
    with pytest.raises(ValueError, match="Стек пустой"):
        stack.pop()


def test_stack_peek_empty():
    """Тест просмотра пустого стека (должна быть ошибка)"""
    stack = Stack()
    with pytest.raises(ValueError, match="Стек пустой"):
        stack.peek()


def test_stack_min_empty():
    """Тест получения минимума из пустого стека (должна быть ошибка)"""
    stack = Stack()
    with pytest.raises(ValueError, match="Стек пустой"):
        stack.min()


def test_stack_single_element():
    """Тест со одним элементом"""
    stack = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.min() == 42
    assert stack.pop() == 42
    assert stack.is_empty() == True


def test_queue_empty():
    """Тест создания пустой очереди"""
    queue = Queue()
    assert queue.is_empty() == True
    assert len(queue) == 0


def test_queue_enqueue():
    """Тест добавления элементов"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert len(queue) == 3
    assert queue.is_empty() == False


def test_queue_dequeue():
    """Тест удаления элементов (FIFO)"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    assert queue.is_empty() == True


def test_queue_front():
    """Тест просмотра первого элемента без удаления"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.front() == 10
    assert len(queue) == 2


def test_queue_dequeue_empty():
    """Тест удаления из пустой очереди (должна быть ошибка)"""
    queue = Queue()
    with pytest.raises(ValueError, match="Очередь пустая"):
        queue.dequeue()


def test_queue_front_empty():
    """Тест просмотра пустой очереди (должна быть ошибка)"""
    queue = Queue()
    with pytest.raises(ValueError, match="Очередь пустая"):
        queue.front()


def test_queue_single_element():
    """Тест с одним элементом"""
    queue = Queue()
    queue.enqueue(42)
    assert queue.front() == 42
    assert queue.dequeue() == 42
    assert queue.is_empty() == True


def test_queue_fifo_order():
    """Тест порядка FIFO"""
    queue = Queue()
    for i in range(1, 6):
        queue.enqueue(i)
    
    result = []
    while not queue.is_empty():
        result.append(queue.dequeue())
    
    assert result == [1, 2, 3, 4, 5]


def test_stack_lifo_order():
    """Тест порядка LIFO"""
    stack = Stack()
    for i in range(1, 6):
        stack.push(i)
    
    result = []
    while not stack.is_empty():
        result.append(stack.pop())
    
    assert result == [5, 4, 3, 2, 1]
