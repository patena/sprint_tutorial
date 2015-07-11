""" Tests for the compute module
"""
from nose.tools import assert_equal

from sprint_tutorial.compute import my_sum


def test_my_sum():
    assert_equal(my_sum(0, 0), 0)
    assert_equal(my_sum(1, 2), 3)
    assert_equal(my_sum(2, 1), 3)
