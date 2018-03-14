""""""


class SparseArray:
    """A Sparse Array that use a linked list implementation."""

    class _Node:
        """A non_public used for storing elements in the SparseArray."""
        def __init__(self, _e, _i, _next, _prev):
            self._e = _e
            self._i = _i
            self._next = next
            self._prev = _prev

    def __init__(self, n):
        self.m = 0
        self.n = n

    def get_usage(self):
        """Prints the amount of elements in the SparseArray."""
        return self.m

    def __len__(self):
        """Prints the capacity of the SparseArray."""
        return self.n

    def __getitem__(self, i):
        """Returns the value of the element at index i."""
        pass

    def __setitem__(self, j, e):
        """Sets the value of element at index j to e."""
        pass

    def fill(self, seq):
        """Add all of the elements from sequence seq into the SparseArray."""
        pass
