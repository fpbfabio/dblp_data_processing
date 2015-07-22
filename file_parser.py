import re
from abs_data import AbsData
from abs_file_parser_factory import AbsFileParserFactory
from abs_file_parser import AbsFileParser
from file_parser_factory import FileParserFactory


class FileParser(AbsFileParser):
    FILE_PERMISSION = "r"
    KEY_ATTRIBUTE = "key="
    TITLE_TAG_START = "<title>"
    TITLE_TAG_END = "</title>"
    MIN_NUMBER_WORDS = 4
    FILE_PATH = ""

    def __init__(self):
        self.__factory = FileParserFactory()

    @property
    def factory(self) -> AbsFileParserFactory:
        return self.__factory

    def parse(self) -> [AbsData]:
        data_list = []
        with open(FileParser.FILE_PATH, FileParser.FILE_PERMISSION) as file:
            key = None
            for line in file:
                key_beginning_index = line.find(FileParser.KEY_ATTRIBUTE) + len(FileParser.KEY_ATTRIBUTE) + 1
                if key_beginning_index != len(FileParser.KEY_ATTRIBUTE):
                    key_end_index = min(line.find("\">"), line.find("\" publtype"))
                    key = line[key_beginning_index:key_end_index]
                title_beginning_index = line.find(FileParser.TITLE_TAG_START) + len(FileParser.TITLE_TAG_START)
                if title_beginning_index != len(FileParser.TITLE_TAG_START) - 1:
                    title_end_index = line.find(FileParser.TITLE_TAG_END)
                    title = line[title_beginning_index:title_end_index]
                    if key is not None:
                        data = self.factory.create_data(key, title)
                        if self._check_data(data):
                            data_list.append(data)
                    key = None
        return data_list

    def _extract_words(self, text: str) -> [str]:
        word = []
        word_dictionary = {}
        count = 0
        letter_or_hyphen_pattern = re.compile(r"[a-z]|[A-Z]|-")
        for character in text:
            if letter_or_hyphen_pattern.match(character) is not None:
                word.append(character)
            else:
                word = str.join("", word)
                word = word.lower().strip("-").strip("-")
                if len(word) > 0 and word not in word_dictionary:
                    word_dictionary[word] = count
                    count += 1
                word = []
        return list(word_dictionary.keys())

    def _check_data(self, data: AbsData) -> bool:
        if ("dblpnote" in data.identifier or
                "&" in data.content or
                len(self._extract_words(data.content)) < FileParser.MIN_NUMBER_WORDS):
            return False
        else:
            return True
