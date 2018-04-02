from sparse_array import SparseArray


sparse_array = SparseArray(10)
sparse_array[1] = 1


print("Testing __setitem__")
try:
    sparse_array[11] = 1
except IndexError:
    print("Got IndexError as excepted")


print("Testing __getitem__")
print("Expecting: 1 got", sparse_array[1])
print("Expecting: None got", sparse_array[2])
try:
    sparse_array[11]
except IndexError:
    print("Got IndexError as excepted")

print("Testing __len__")
print("Expecting: 10 got", len(sparse_array))

print("Testing get_usage")
print("Expecting: 1 got", sparse_array.get_usage())

print("Testing fill")
try:
    sparse_array.fill([n for n in range(1, 15)])
except ValueError:
    print("Got ValueError as expected")

print("Testing fill")
seq = [n for n in range(2)]
print(sparse_array.get_usage())
sparse_array.fill(seq)
print(sparse_array.get_usage())
