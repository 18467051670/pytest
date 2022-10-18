import pytest


class Test0(object):
    def setup_class(self):  # 在每个class的开始和结束各执行一次
        pass

    def teardown_class(self):
        pass

    def setup_method(self):  # 在每个方法前后执行一次
        pass

    def teardown_method(self):
        pass

    @pytest.mark.L1
    @pytest.mark.L2
    def test_a(self):
        print('aaa')
        assert 5 > 3

    @pytest.mark.L1
    def test_b(self):
        print('bbb')
        assert 'Strom' in 'Hello Strom'


class Test03_02(object):
    def setup_class(self):  # 在每个class的开始和结束各执行一次
        pass

    def teardown_class(self):
        pass

    def setup_method(self):  # 在每个方法前后执行一次
        pass

    def teardown_method(self):
        pass

    @pytest.mark.L1
    def test_c(self):
        print('ccc')
        assert 'c' == 'c'
        print()

    @pytest.mark.L3
    def test_d(self):
        print('ddd')
        assert 'd' == 'd'


if __name__ == '__main__':
    pytest.main(["-s", "Pytest03.py"])
    # pytest.main(["-s", "Pytest03.py::Test03_02"])
