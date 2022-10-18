import pytest


class TestStorm(object):
    def setup_module(self):  # 在整个文件的开始和结束执行一次
        print('setup_module')

    def teardown_module(self):
        print('teardown_module')

    def setup_function(self):  # 在每个函数前后执行一次
        print('setup_function')

    def teardown_function(self):
        print('teardown_function')

    def setup_class(self):  # 在每个class的开始和结束各执行一次
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):  # 在每个方法前后执行一次
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_a(self):
        print('a')
        assert 'a' == 'a'

    def test_b(self):
        print('b')
        assert 'b' == 'b'


if __name__ == '__main__':
    pytest.main(["-s", "Pytest01.py"])
