class Television:
    """
    Class representing details for a remote object
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor that creates the initial state of the television object
        sets channel and volume to their minimums and status to off
        :return: None
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method that sets the status of the TV to it's opposite when called
        :return: None
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method to raise the channel of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to lower the channel of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to raise the volume of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to lower the volume of the TV object by one
        :return: None
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def get_channel(self) -> int:
        """
        Method to get channel value
        :return: Channel (int)
        """
        return self.__channel

    def get_volume(self) -> int:
        """
        Method to get volume value
        :return: Volume (int)
        """
        return self.__volume

    def get_status(self) -> bool:
        """
        Method to get status
        :return: Status (bool)
        """
        return self.__status

    def __str__(self) -> str:
        """
        Method to return the current state of the TV object
        :return: The status, channel, and volume of the TV object
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
