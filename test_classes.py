import unittest
from classes import *


class Test:
    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test_init(self):
        assert self.tv_1.

    def test_power(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass

    def test_str(self):
        pass


if __name__ == '__main__':
    unittest.main()
