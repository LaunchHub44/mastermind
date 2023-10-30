import pytest
import hit_n_blow

def test_ansToTuple():
    assert hit_n_blow.ansToTuple("000") == (0, 0, 0)