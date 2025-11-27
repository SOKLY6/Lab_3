from benchmarks.benchmark import benchmark


class Queue:
    """Реализация очереди на основе односвязного списка."""

    class __Node:
        """Узел односвязного списка."""

        def __init__(self, value: int) -> None:
            """
            Инициализирует узел.

            Args:
                value: Значение узла.
            """
            self.value = value
            self.next: Queue.__Node | None = None

    def __init__(self) -> None:
        """Инициализирует пустую очередь."""
        self.head: Queue.__Node | None = None
        self.tail: Queue.__Node | None = None
        self.length = 0

    @benchmark
    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.

        Returns:
            True, если очередь пуста, иначе False.
        """
        return self.head is None

    @benchmark
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.

        Returns:
            Размер очереди.
        """
        return self.length

    @benchmark
    def dequeue(self) -> int:
        """
        Удаляет и возвращает элемент из начала очереди.

        Returns:
            Значение удалённого элемента.

        Raises:
            ValueError: Если очередь пустая.
        """
        if self.head is None:
            raise ValueError('Очередь пустая')
        if self.head.next is None:
            value = self.head.value
            self.head = self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next
        self.length -= 1
        return value

    @benchmark
    def enqueue(self, value: int) -> None:
        """
        Добавляет элемент в конец очереди.

        Args:
            value: Значение для добавления.
        """
        new_node = self.__Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            if self.tail is not None:
                self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    @benchmark
    def front(self) -> int:
        """
        Возвращает элемент из начала очереди без удаления.

        Returns:
            Значение первого элемента.

        Raises:
            ValueError: Если очередь пустая.
        """
        if self.head is None:
            raise ValueError('Очередь пустая')
        return self.head.value
