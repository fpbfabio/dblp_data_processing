""""
Module with an abstract class for serializing AbsData objects to xml.
"""

from abc import ABCMeta, abstractmethod

from abs_data import AbsData


class AbsXmlSerializer(metaclass=ABCMeta):
    """"
    Class for serializing AbsData objects to xml.
    """
    @abstractmethod
    def serialize(self, data_list: [AbsData]) -> None:
        """
        Serializes the given AbsData object to a xml file.
        """
        pass
