import unittest
from src.Queue.DualStack_Queue import DualStack_Queue

class TestDualStackQueue(unittest.TestCase):
        def setUp(self):
            self.queue = DualStack_Queue()
            self.input = [1,2,3]
        
        def test_push_should_work_for_multiple_items(self):
              for item in self.input:
                self.queue.push(item)
              self.assertEqual(self.input, self.queue.enqeue)

        def test_pop_should_work_for_multiple_items(self):
            for item in self.input:
                self.queue.push(item)
            self.assertEqual(self.input[0], self.queue.pop())

        def test_peek_should_work_for_multiple_items(self):
            for item in self.input:
                self.queue.push(item)
            self.assertEqual(self.input[0], self.queue.peek())
              
        def test_empty_should_work_for_multiple_items(self):
            for item in self.input:
                self.queue.push(item)
                self.queue.pop()
            self.assertEqual(True, self.queue.empty())