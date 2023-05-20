import pytest
from stack_and_queue.stack_and_queue import Stack, Queue


def test_stack_push():
    stack = Stack()
    stack.push(10)
    assert stack.top.value == 10


def test_stack_push_multiple():
    stack = Stack()
    stack.push(22)
    stack.push(33)
    stack.push(44)
    assert stack.top.value == 44


def test_stack_pop():
    stack = Stack()
    stack.push(10)
    value = stack.pop()
    assert value == 10
    assert stack.top is None


def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_stack_peek():
    stack = Stack()
    stack.push(10)
    value = stack.peek()
    assert value == 10
    assert stack.top.value == 10


def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


def test_stack_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(10)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True


def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(11)
    assert queue.front.value == 11
    assert queue.rear.value == 11


def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(11)
    queue.enqueue(22)
    queue.enqueue(33)
    assert queue.front.value == 11
    assert queue.rear.value == 33


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(10)
    value = queue.dequeue()
    assert value == 10
    assert queue.front is None
    assert queue.rear is None


def test_queue_dequeue_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_queue_peek():
    queue = Queue()
    queue.enqueue(10)
    value = queue.peek()
    assert value == 10
    assert queue.front.value == 10


def test_queue_peek_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()


def test_queue_empty():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(10)
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True