# Implementation of the lazy approach to union-find: quick-union.

class QuickUnion_UnionFind:
    """ Implementation of the eager approach to union-find: quick-find. """
    id = [] # Our list of ids.

    def __init__(self, n: int):
        self.id = list(range(n)) # Generate a list of ids to populate from 0 .. N.

    def __repr__(self):
        return f"<QuickUnion_UnionFind id:{self.id}>"
    
    def _check_indicies(func):
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

    def _root(self, root_of_i: int):
        """ Find root of given index, O(N) """
        _root_of_i = root_of_i
        while _root_of_i != self.id[_root_of_i]:
            _root_of_i = self.id[_root_of_i]
        return _root_of_i

    @_check_indicies
    def connected(self, p: int, q: int):
        """ Check if two roots are the same, O(N)"""
        return self._root(p) == self._root(q)
    
    
    @_check_indicies
    def union(self, p: int, q: int):
        """ Transform p root to q root, O(1)"""
        p_root = self._root(p)
        q_root = self._root(q)
        self.id[p_root] = q_root
        
