class DualStack_Queue:
    def __init__(self):
        self.enqeue = []
        self.dequeue = []

    def fill_dequeue(func) -> None:
        """
            Decorator for pop and peek.
            Fill the dequeue if it is empty.
            This reverses the order of the original enqueue stack.
            Thus putting the 1st item on the top of the stack.
            O(N) time complexity.
        """
        def wrapper(self):
            if (len(self.dequeue) == 0):
                while(len(self.enqeue) > 0):
                    self.dequeue.append(self.enqeue.pop())
            return func(self)
        return wrapper

    def push(self, item: int) -> None:
        """
            Enqueue an item.
            O(1) time complexity.
        """
        self.enqeue.append(item)

    @fill_dequeue
    def pop(self) -> int:
        """
            Pop the last item off of the deqeue.
            Or, otherwise, pop the first item on the queue.
            O(N) due to te underlying decorator.
        """
        return self.dequeue.pop()
    
    @fill_dequeue
    def peek(self) -> int:
        """
            Look at the last item off of the deqeue.
            Or, otherwise, look at the first item on the queue.
            O(N) due to the underlying decorator.
        """
        return self.dequeue[len(self.dequeue) - 1]
    
    def empty(self) -> bool:
        return len(self.dequeue) == 0 and len(self.enqeue) == 0