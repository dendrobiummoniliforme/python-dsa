# Implementation of the eager approach to union-find: quick-find.

class QuickFind_UnionFind:
    """ Implementation of the eager approach to union-find: quick-find. """
    id = [] # Our list of ids.

    def __init__(self, n: int):
        self.id = list(range(n)) # Generate a list of ids to populate from 0 .. N.

    def __repr__(self):
        return f"<QuickFind_UnionFind id:{self.id}>"
    
    def check_indicies(func):
        """ 
            Check indicies provided by user input. 
            See https://pythonforthelab.com/blog/how-to-use-decorators-to-validate-input/
        """
        def wrapper(self, p: int, q: int):
            length_of_id_list = len(self.id)
            if (p > length_of_id_list or q > length_of_id_list) or (p < 0 or q < 0):
                raise Exception("Union input is invalid index.")
            return func(self, p, q)
        return wrapper

    @check_indicies
    def connected(self, p: int, q: int):
        """ Check if two ids are the same, O(1)"""
        return self.id[p] == self.id[q]
    
    @check_indicies
    def union(self, p: int, q: int):
        """ Transform all p to q, O(N)"""
        p_id = self.id[p]
        q_id = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
        

