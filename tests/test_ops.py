from src.math_ops import sum, sub

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    assert sum(-1, -1) == -2

def test_sub():
    assert sub(2, 3) == -1
    assert sub(-1, 1) == -2
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0