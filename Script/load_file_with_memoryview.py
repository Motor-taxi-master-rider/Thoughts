# -*- coding: utf-8 -*-
import os
from time import time

# 大文件名
FILENAME = r'C:\Users\chu060\Downloads\ubuntu-16.04.2-desktop-i386.iso'


def test_load_file_copy():
    """使用普通的读取字节流的方式，该方式会进行一次拷贝"""
    f = open(FILENAME, 'rb')
    buf = bytearray(f.read())
    f.close()
    return buf[:100]


def test_load_file_mv():
    """memoryview测试"""
    f = open(FILENAME, 'rb')
    buf = bytearray(os.path.getsize(FILENAME))
    mv = memoryview(buf)
    f.readinto(mv)
    f.close()
    return buf[:100]


def test_load_file_ba():
    """无memoryview，使用bytearray"""
    f = open(FILENAME, 'rb')
    buf = bytearray(os.path.getsize(FILENAME))
    f.readinto(buf)
    f.close()
    return buf[:100]


def load_tester(func, n=3):
    """进行测试并输出结果"""
    print('=' * 50)
    start = time()
    for i in range(n):
        result = func()
        if i == 0:
            print(result)
    print('try {test_times} times, {name} avg running time: {avg_time}'.format(
        test_times=n,
        name=func.__name__,
        avg_time=str((time() - start) / n)))


# 获取所有待测函数
test_funcs = [globals()[name] for name in globals() if name.startswith('test')]
# 进行测试,此处取十次测试的平均值
for func in test_funcs:
    load_tester(func, 10)
