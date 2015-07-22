""""
Module with an abstract factory class.
"""

from abc import ABCMeta, abstractmethod

from abs_data import AbsData


class AbsFileParserFactory(metaclass=ABCMeta):
    """"
    Factory class.
    """

    @abstractmethod
    def create_data(self, identifier: str, content: str) -> AbsData:
        """
        Instantiates an object derived from the AbsData class.
        """
        pass
