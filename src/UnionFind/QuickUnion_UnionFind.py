

class QuickUnion_UnionFind:
    """ 
        Implementation of the lazy approach to union-find: quick-union.
    """
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

    def find(self, root_of_i: int):
        """ 
            Find root of given index, O(N).
            Traverse tree until the given id matches the expected root.
        """
        while root_of_i != self.id[root_of_i]:
            root_of_i = self.id[root_of_i]
        return root_of_i

    @_check_indicies
    def connected(self, p: int, q: int):
        """ 
            Check if two roots are connected, O(N).
        """
        return self.find(p) == self.find(q)
    
    
    @_check_indicies
    def union(self, p: int, q: int):
        """
            Transform p root to q root, O(1)
        """
        p_root = self.find(p)
        q_root = self.find(q)
        self.id[p_root] = q_root 
        
