import unittest
from classes import *


class Test:
    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test_init(self):
        assert self.tv_1.get_channel() == 0
        assert self.tv_1.get_volume() == 0
        assert self.tv_1.get_status() == False

    def test_power(self):
        self.tv_1.power()
        assert self.tv_1.get_status() == True
        self.tv_1.power()
        assert self.tv_1.get_status() == False

    def test_channel_up(self):
        self.tv_1.channel_up()
        assert self.tv_1.get_channel() == 0

        self.tv_1.power()

        self.tv_1.channel_up()
        assert self.tv_1.get_channel() == 1
        self.tv_1.channel_up()
        assert self.tv_1.get_channel() == 2
        self.tv_1.channel_up()
        assert self.tv_1.get_channel() == 3
        self.tv_1.channel_up()
        assert self.tv_1.get_channel() == 0

    def test_channel_down(self):
        self.tv_1.channel_down()
        assert self.tv_1.get_channel() == 0

        self.tv_1.power()

        self.tv_1.channel_down()
        assert self.tv_1.get_channel() == 3
        self.tv_1.channel_down()
        assert self.tv_1.get_channel() == 2
        self.tv_1.channel_down()
        assert self.tv_1.get_channel() == 1
        self.tv_1.channel_down()
        assert self.tv_1.get_channel() == 0

    def test_volume_up(self):
        self.tv_1.volume_up()
        assert self.tv_1.get_volume() == 0

        self.tv_1.power()
        self.tv_1.volume_up()
        assert self.tv_1.get_volume() == 1
        self.tv_1.volume_up()
        assert self.tv_1.get_volume() == 2
        self.tv_1.volume_up()
        assert self.tv_1.get_volume() == 2

    def test_volume_down(self):
        self.tv_1.volume_down()
        assert self.tv_1.get_volume() == 0

        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        assert self.tv_1.get_volume() == 2

        self.tv_1.volume_down()
        assert self.tv_1.get_volume() == 1
        self.tv_1.volume_down()
        assert self.tv_1.get_volume() == 0
        self.tv_1.volume_down()
        assert self.tv_1.get_volume() == 0


    def test_str(self):
        assert self.tv_1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 1'

if __name__ == '__main__':
    unittest.main()
