import pytest
import os
from math_operations import basic_math_operation

def test_add():
    assert basic_math_operation(2, 3, 'add') == 5
    assert basic_math_operation(-2, 3, 'add') == 1
    assert basic_math_operation(0, 0, 'add') == 0

def test_subtract():
    assert basic_math_operation(5, 3, 'subtract') == 2
    assert basic_math_operation(2, 5, 'subtract') == -3
    assert basic_math_operation(0, 0, 'subtract') == 0

if os.getenv("RUN_GPU_TESTS") == "true":
    def test_multiply():
        assert basic_math_operation(2, 3, 'multiply') == 6
        assert basic_math_operation(-2, 3, 'multiply') == -6
        assert basic_math_operation(0, 5, 'multiply') == 0

    def test_divide():
        assert basic_math_operation(6, 3, 'divide') == 2
        assert basic_math_operation(7, 2, 'divide') == 3.5

        with pytest.raises(ValueError):
            basic_math_operation(6, 0, 'divide')

    def test_invalid_operation():
        with pytest.raises(ValueError):
            basic_math_operation(2, 3, 'modulus')
