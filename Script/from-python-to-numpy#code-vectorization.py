import numpy as np


def find_index(Z1, Z2):
    step = Z2.strides[0] // Z1.strides[0]
    assert step
    offset_start = abs(np.byte_bounds(Z2)[0] - np.byte_bounds(Z1)[0])
    offset_stop = abs(np.byte_bounds(Z2)[-1] - np.byte_bounds(Z1)[-1])
    start = offset_start // Z1.itemsize
    stop = Z1.size - offset_stop // Z1.itemsize
    if step < 0:
        start, stop = stop - 1, start - 1
    print(start, stop, step)
    assert np.allclose(Z1[start:stop:step], Z2)


Z1 = np.arange(10)
Z2 = Z1[1:-1:2]
find_index(Z1, Z2)
Z2 = Z1[-1:0:-2]
find_index(Z1, Z2)
Z1.reshape(2, 5)
Z2 = Z1[-1:0:-2]
find_index(Z1, Z2)
