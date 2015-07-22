""""
Module with an abstract class for parsing files into AbsData objects.
"""

from abc import ABCMeta, abstractmethod

from abs_data import AbsData
from abs_file_parser_factory import AbsFileParserFactory


class AbsFileParser(metaclass=ABCMeta):
    """"
    Class for parsing files into AbsData objects.
    """
    @property
    @abstractmethod
    def factory(self) -> AbsFileParserFactory:
        """
        Returns an object of type AbsFactory.
        """
        pass

    @abstractmethod
    def parse(self) -> [AbsData]:
        """
        Serializes the given AbsData object to a xml file.
        """
        pass
