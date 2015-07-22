""""
Module with an abstract factory class.
"""
from abs_file_parser_factory import AbsFileParserFactory
from abs_data import AbsData
from data import Data

class FileParserFactory(AbsFileParserFactory):

    def create_data(self, identifier: str, content: str) -> AbsData:
        return Data(identifier, content)
