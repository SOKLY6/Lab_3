from benchmarks.benchmark import benchmark


class Stack:
    """Реализация стека на основе односвязного списка."""

    class __Node:
        """Узел односвязного списка с хранением минимума."""

        def __init__(self, value: int) -> None:
            """
            Инициализирует узел.

            Args:
                value: Значение узла.
            """
            self.value = value
            self.next: Stack.__Node | None = None
            self.minimum = value

    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self.head: Stack.__Node | None = None
        self.tail: Stack.__Node | None = None
        self.length = 0

    @benchmark
    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        Returns:
            True, если стек пуст, иначе False.
        """
        return self.head is None

    @benchmark
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.

        Returns:
            Размер стека.
        """
        return self.length

    @benchmark
    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека.

        Args:
            value: Значение для добавления.
        """
        new_node = self.__Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.minimum = min(self.head.minimum, new_node.value)
            self.head = new_node
        self.length += 1

    @benchmark
    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке за O(1).

        Returns:
            Минимальное значение в стеке.

        Raises:
            ValueError: Если стек пустой.
        """
        if self.head is None:
            raise ValueError('Стек пустой')
        return self.head.minimum

    @benchmark
    def pop(self) -> int:
        """
        Удаляет и возвращает элемент с вершины стека.

        Returns:
            Значение удалённого элемента.

        Raises:
            ValueError: Если стек пустой.
        """
        if self.head is None:
            raise ValueError('Стек пустой')
        result = self.head.value
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return result

    @benchmark
    def peek(self) -> int:
        """
        Возвращает элемент с вершины стека без удаления.

        Returns:
            Значение верхнего элемента.

        Raises:
            ValueError: Если стек пустой.
        """
        if self.head is None:
            raise ValueError('Стек пустой')
        return self.head.value
