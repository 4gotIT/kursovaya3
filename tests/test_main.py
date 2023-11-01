import os

import pytest
from utils.funcs import load_data, sorted_list


def test_load_data():
    assert load_data('') is None
    assert load_data('path') is None

def test_sorted_list():
