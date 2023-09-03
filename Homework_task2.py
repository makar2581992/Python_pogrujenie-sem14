import pytest
from Bank import nal

@pytest.fixture()
def make_bank():
    return nal()


def test_in():
    bank = nal()
    assert bank._in(10000, 10) == (20010, 1)


def test_out(make_bank):
    assert make_bank._out(5000, 1000, 2000) == (2000, 1)


if __name__ == '__main__':
    pytest.main(['-v'])