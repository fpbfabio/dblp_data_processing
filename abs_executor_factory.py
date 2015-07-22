""""
Module with an abstract factory class to create objects used in AbsExecutor objects.
"""

from abc import ABCMeta, abstractmethod

from abs_file_parser import AbsFileParser
from abs_xml_serializer import AbsXmlSerializer


class AbsExecutorFactory(metaclass=ABCMeta):
    """"
    Factory class to create objects used in AbsExecutor objects.
    """

    @abstractmethod
    def create_file_parser(self) -> AbsFileParser:
        """
        Instantiates an object derived from the AbsFileParser class.
        """
        pass

    @abstractmethod
    def create_xml_serializer(self) -> AbsXmlSerializer:
        """
        Instantiates an object derived from the AbsXmlSerializer class.
        """
        pass
