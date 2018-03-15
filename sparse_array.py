""""""


class SparseArray:
    """A Sparse Array that use a linked list implementation."""

    class _Node:
        """A non_public used for storing elements in the SparseArray."""
        def __init__(self, _e, _i, _next, _prev):
            self._e = _e
            self._i = _i
            self._next = _next
            self._prev = _prev

    def __init__(self, n):
        self.m = 0
        self.n = n
        self.tail = self._Node(None, None, None, None)
        self.head = self._Node(None, None, None, None)
        self.head._next = self.tail
        self.tail._prev = self.head

    def get_usage(self):
        """Prints the amount of elements in the SparseArray."""
        return self.m

    def _get_node_at(self, i, node):
        """A recursive function that will return the node at index i."""
        if node is self.tail:
            return None
        elif node._i == i:
            return node
        else:
            return self._get_node_at(i, node._next)

    def _make_node(self, e, i):
        """Makes a new node containing element e at index i"""
        new_node = self._Node(e, i, self.tail, self.tail._prev)
        self.tail._prev._next = new_node
        self.tail._prev = new_node

    def __len__(self):
        """Prints the capacity of the SparseArray."""
        return self.n

    def __getitem__(self, i):
        """Returns the value of the element at index i."""
        if i > self.n:
            raise IndexError
        return self._get_node_at(i, self.head._next)

    def __setitem__(self, j, e):
        """Sets the value of element at index j to e."""
        if j > self.n:
            raise IndexError
        node = self._get_node_at(j, self.head._next)
        if node == None:
            self._make_node(e, j)
        else:
            node._e = e
            # TODO: Need to be able to set an element to None correctly.

    def fill(self, seq):
        """Add all of the elements from sequence seq into the SparseArray."""
        if self.n < self.m + len(seq):
            raise ValueError
