""""""


class SparseArray:
    """A Sparse Array that use a linked list implementation."""

    class _Node:
        """A non_public used for storing elements in the SparseArray."""
        def __init__(self, _e, _i, _next):
            self._e = _e
            self._i = _i
            self._next = _next

    def __init__(self, n):
        self.m = 0
        self.n = n
        self.tail = self._Node(None, None, None)
        self.head = self._Node(None, None, self.tail)

    def get_usage(self):
        """Prints the amount of elements in the SparseArray."""
        return self.m

    def __len__(self):
        """Prints the capacity of the SparseArray."""
        return self.n

    def __getitem__(self, i):
        """Returns the value of the element at index i."""
        if i > self.n:
            raise IndexError

    def __setitem__(self, j, e):
        """Sets the value of element at index j to e."""
        if j > self.n:
            raise IndexError

    def fill(self, seq):
        """Add all of the elements from sequence seq into the SparseArray."""
        if self.n < self.m + len(seq):
            raise ValueError
