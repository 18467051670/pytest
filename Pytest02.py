import pytest


def test_c():
    print('ccc')
    assert 'c' == 'c'


class Test01(object):
    def test_a(self):
        print('aaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbb')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s", "Pytest02.py"])
