import data_structures as ds


def run_test_stack():
    stack = ds.Stack([1, 2, 3, 4, 5])

    # wrong push value test
    stack.push()

    print("Init top of the stack: " + str(stack.top))

    stack.push(6)
    top_pointer_experimental = stack.top

    print("New top of the stack: " + str(stack.top))
    print("Is stack empty? " + str(stack.is_empty))

    top_element = stack.pop
    top_pointer_1 = stack.top

    print("Top of the stack after 'pop': " + str(stack.top))
    print("Top element of the stack was: " + str(top_element))

    top_element_2 = stack.pop
    top_pointer_2 = stack.top

    print("Top of the stack after 2nd 'pop': " + str(stack.top))
    print("Top element of the stack was: " + str(top_element_2))

    # emptiness test
    top_element_3 = stack.pop
    top_pointer_3 = stack.top
    top_element_4 = stack.pop
    top_pointer_4 = stack.top
    top_element_5 = stack.pop
    top_pointer_5 = stack.top
    top_element_6 = stack.pop
    top_pointer_6 = stack.top
    top_element_7 = stack.pop
    top_pointer_7 = stack.top

    print("Is stack empty? " + str(stack.is_empty))

    stack_docs = ds.Stack.__doc__
    print(stack_docs)


def run_test_queue():
    queue = ds.Queue([1, 2, 3, 4, 5], queue_length=10)

    first_element = queue.dequeue
    print(first_element)

    out_element = queue.dequeue
    print(out_element)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))

    # emptiness test
    first_element_2 = queue.dequeue
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    first_element_3 = queue.dequeue
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    first_element_4 = queue.dequeue
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    first_element_5 = queue.dequeue
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    first_element_6 = queue.dequeue
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))

    # overflow test
    queue.enqueue(6)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(7)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(8)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(9)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(10)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(11)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(12)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(13)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(14)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(15)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))

    out_element = queue.dequeue
    print(out_element)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))
    queue.enqueue(12)
    print("Head is: " + str(queue.head) + "; tail is: " + str(queue.tail))


def run_test_linked_list():
    test_linked_list = ds.LinkedList()

    test_linked_list.list_insert(5)
    test_linked_list.list_insert('ten')
    test_linked_list.list_insert(15)
    test_linked_list.list_insert(20)
    test_linked_list.list_insert(25)

    search_node = test_linked_list.list_search(15)
    search_node.key = 17

    test_linked_list.list_delete(search_node)
    print(test_linked_list.head)


run_test_stack()
# run_test_queue()
# run_test_linked_list()
