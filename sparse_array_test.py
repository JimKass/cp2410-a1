from sparse_array import SparseArray
import time
import sys


def experiment_memory_usage():
    pass


def experiment_setitem(n):
    sparse_array = SparseArray(n)
    for i in range(n):
        sparse_array[i - 1] = i
    start_time = time.time()
    sparse_array[n - 1] = "This one"
    end_time = time.time()
    return end_time - start_time


def experiment_getitem(n):
    sparse_array = SparseArray(n)
    for i, e in enumerate([i for i in range(n)]):
        sparse_array[i] = e
    start_time = time.time()
    x = sparse_array[n - 1]
    end_time = time.time()
    return end_time - start_time


def experiment_fill(n):
    sparse_array = SparseArray(n)
    seq = [i for i in range(n)]
    start_time = time.time()
    sparse_array.fill(seq)
    end_time = time.time()
    return end_time - start_time


def main():
    number_of_tests = 1
    testing_amounts = [i for i in range(1, 101)]
    sys.setrecursionlimit(1000000010)
    print("Testing results for SparseArray.__getitem__\n")
    for n in testing_amounts:
        setitem_results = []
        for i in range(number_of_tests):
            setitem_results.append(experiment_setitem(n))
        print("{:13s} {}".format(str(n), str(sum(setitem_results) / len(setitem_results))))

    print("\nTesting results for SparseArray.__setitem__\n")
    for n in testing_amounts:
        getitem_results = []
        for i in range(number_of_tests):
            getitem_results.append(experiment_getitem(n))
        print("{:13s} {}".format(str(n), str(sum(getitem_results) / len(getitem_results))))

    print("\nTesting results for SparseArray.fill\n")
    for n in testing_amounts:
        fill_results = []
        for i in range(number_of_tests):
            fill_results.append(experiment_fill(n))
        print("{}, {}".format(str(n), str(sum(fill_results) / len(fill_results))))

main()
