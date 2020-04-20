"""
Module contains data structures such as:

1) Stack: LIFO (last-in, first-out) strategy.
2) Queue: FIFO (first-in, first-out) strategy.
3) Linked List.
4) Binary Tree.
"""


class EmptyInput(Exception): pass


class Stack:
    """
    Stack input -- set of numbers.
    Stack operations:
        top -- index of the rightmost element;
        push(value) -- add value to the top;
        pop -- returns value from the top;
        is_empty -- returns True if there are no elements in stack.
    """

    __top = 0

    def __init__(self, stack_array=None):
        self.__array = stack_array
        if stack_array is not None:
            self.__top = len(stack_array) - 1
        else:
            self.__top = - 1

    def push(self, new_element=None):
        try:
            if new_element is None:
                raise EmptyInput
            else:
                self.__array.append(new_element)
                self.__top += 1
        except EmptyInput:
            print("There is no element to push to the stack!")

    @property
    def pop(self):
        if self.is_empty:
            print("Stack is empty!")
            return 0
        else:
            self.__top -= 1
            return self.__array[self.top + 1]

    @property
    def top(self):
        return self.__top

    @property
    def is_empty(self):
        return self.top == -1


class Queue:
    """
    Queue input -- set of numbers.
    Queue operations:
        tail -- pointer to the end of the set;
        head -- pointer to the first element of the set;
        enqueue -- put element to the queue;
        dequeue -- extract element from the queue.
    Queue is cyclically closed: after n-1 cell index goes 0 index cell.
    """

    __head, __tail = 0, 0

    def __init__(self, queue_array=None, queue_length=0):
        try:
            if queue_array is not None:
                if queue_length < len(queue_array):
                    print("Wrong queue set length relative to the adjusted elements array!")
                else:
                    self.__array = queue_array
                    self.__queue_length = queue_length
                    self.__tail = len(queue_array)
                    while queue_length > len(self.__array):
                        self.__array.append(0)
            else:
                raise EmptyInput
        except EmptyInput:
            print("Queue init input is empty!")

    def enqueue(self, new_element):
        if not self.is_full:
            self.__array[self.__tail] = new_element
            if self.__tail == self.__queue_length - 1:
                self.__tail = 0
            else:
                self.__tail += 1
        else:
            print("Queue is full!")

    @property
    def dequeue(self):
        if not self.is_empty:
            output_element = self.__array[self.__head]
            if self.__head - 1 == self.__queue_length:
                self.__head = 0
            else:
                self.__head += 1
            return output_element
        else:
            print("Queue is empty!")
            return 0

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def is_empty(self):
        return self.__head == self.__tail

    @property
    def is_full(self):
        init_full = self.__head == 0 and self.__tail == self.__queue_length - 1
        tail_catch_head = self.__head == self.__tail + 1
        return tail_catch_head or init_full


class ListNode:
    """
    Linked list element (item). If has pointer to the previous and next list elements.
    """
    __slots__ = ("prev", "key", "next")
    # 'slots' helps to block the creation of attributes other than declared

    def __init__(self, prev, key, _next):
        self.prev = prev
        self.key = key
        self.next = _next

    def __str__(self):
        return "ListNode"


class LinkedList:
    """
    A set of List Node objects. Each object points to its neighboring elements (previous and next).
    Methods:
        list_insert -- add value in the very beginning (head) of the list;
        list_search -- find value through sequential viewing;
        list_delete -- removes node from the list.
    """

    def __init__(self):
        self.__head = None

    def list_insert(self, value):
        new_element = ListNode(None, value, self.__head)
        if self.__head is not None:
            self.__head.prev = new_element
        self.__head = new_element

    def list_search(self, value):
        node = self.__head
        while node is not None and node.key != value:
            node = node.next
        return node

    def list_delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.__head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    @property
    def head(self):
        return self.__head

    def __str__(self):
        return "LinkedList"
