""""
Module with an abstract class that represents the data taken from a search engine.
"""

from abc import ABCMeta, abstractmethod


class AbsData(metaclass=ABCMeta):
    """"
    Class that represents the data taken from a search engine.
    """

    @property
    @abstractmethod
    def identifier(self) -> str:
        """
        A unique identifier for the data in the scope of the search engine.
        """
        pass

    @property
    @abstractmethod
    def content(self) -> str:
        """
        Text content of the data.
        """
        pass
