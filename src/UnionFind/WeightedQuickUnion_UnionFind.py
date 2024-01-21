class WeightedQuickUnion_UnionFind:
    """ 
        Implementation of the weighted approach to union-find: weighted quick-union. 
    """
    id = [] # Our list of ids.
    size = [] # Our list of tree sizes.

    def __init__(self, n: int):
        self.id = list(range(n)) # Generate a list of ids to populate from 0 .. N.
        self.size = list(range(n)) # Generate a size list to populate of length <= N.
        for i in range(n):
           self.size[i] = 1 # All roots are trees of size 1 before we union any of them.

    def __repr__(self):
        return f"<WeightedQuickUnion_UnionFind id, size:{self.id, self.size}>"
    
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
        """
        while root_of_i != self.id[root_of_i]:
            root_of_i = self.id[root_of_i]
        return root_of_i

    @_check_indicies
    def connected(self, p: int, q: int):
        """ 
            Check if two roots are the same, O(N).
        """
        return self.find(p) == self.find(q)
    
    
    @_check_indicies
    def union(self, p: int, q: int):
        """ 
            Transform p root to q root, O(1).
            Weighted variant.
            Set the tree to point in a certain direction dependent on the 
            size of the current root's tree.
            Update the trees size to be itself plus the new tree.
        """
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] = self.size[q_root] + self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] = self.size[p_root] + self.size[q_root]
        
