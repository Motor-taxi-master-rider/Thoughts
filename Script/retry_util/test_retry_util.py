
import unittest
from itertools import repeat

from unittest.mock import patch

from retry_util import retry

_STACK = []


class TestRetryUtil(unittest.TestCase):
    def setUp(self):
        global _STACK  # pylint: disable=global-statement
        _STACK = [i for i in range(5)]  # reset stack to [0 1 2 3 4] <-top
        self.addCleanup(patch.stopall)

    def test_without_retry(self):
        self.assertFalse(function_equal_without_retry(1))
        self.assertEqual(_STACK[-1], 3)

    def test_raise_exception(self):
        self.assertTrue(function_equal_with_exception(1))
        self.assertEqual(_STACK[-1], 0)

    def test_match_result(self):
        self.assertTrue(function_equal_with_match_result(1))
        self.assertEqual(_STACK[-1], 0)

    def test_match_result_failed(self):
        with self.assertRaises(IndexError):
            # pop from empty list
            self.assertFalse(function_equal_with_match_result_fail(-1))
        self.assertEqual(len(_STACK), 0)

    def test_match_retry_once(self):
        self.assertFalse(function_equal_retry_once(1))
        self.assertEqual(_STACK[-1], 2)

    def test_both_catch_exception_and_match_result(self):
        self.assertTrue(function_equal_with_exception_and_match_result(1))
        self.assertEqual(_STACK[-1], 0)

    def test_retry_on_static_method(self):
        mock_class = MockRetryClass()
        self.assertTrue(mock_class.static_equal(1))
        self.assertEqual(_STACK[-1], 0)

    def test_retry_on_class_method(self):
        self.assertTrue(MockRetryClass.class_equal(1))
        self.assertEqual(_STACK[-1], 0)

    def test_retry_on_instance_method(self):
        mock_class = MockRetryClass()
        self.assertTrue(mock_class.instance_equal(1))
        self.assertEqual(_STACK[-1], 0)


class _MockException1(Exception):
    pass


class _MockException2(Exception):
    pass


def _match_true(result):
    return result is True


def function_equal_without_retry(num):
    return num == _STACK.pop()


@retry(catch_exceptions=(_MockException1, _MockException2), delays=repeat(0.1, 5))
def function_equal_with_exception(num):
    if num == _STACK.pop():
        return True
    elif num % 2 == 1:
        # odd
        raise _MockException1()
    elif num % 2 == 0:
        # even
        raise _MockException2()


@retry(match_result=_match_true, delays=repeat(0.1, 5))
def function_equal_with_match_result(num):
    return num == _STACK.pop()


@retry(match_result=_match_true, delays=repeat(0.1, 5))
def function_equal_with_match_result_fail(num):
    return num == _STACK.pop()


@retry(match_result=_match_true, delays=repeat(0.1, 1))
def function_equal_retry_once(num):
    return num == _STACK.pop()


@retry(catch_exceptions=(_MockException1,), match_result=_match_true, delays=repeat(0.1, 5))
def function_equal_with_exception_and_match_result(num):
    if num == _STACK.pop():
        return True
    elif num % 2 == 1:
        # odd
        raise _MockException1()
    elif num % 2 == 0:
        # even
        return False


class MockRetryClass(object):
    @staticmethod
    @retry(match_result=_match_true, delays=repeat(0.1, 5))
    def static_equal(num):
        return num == _STACK.pop()

    @classmethod
    @retry(match_result=_match_true, delays=repeat(0.1, 5))
    def class_equal(cls, num):
        return num == _STACK.pop()

    @retry(match_result=_match_true, delays=repeat(0.1, 5))
    def instance_equal(self, num):
        return num == _STACK.pop()
