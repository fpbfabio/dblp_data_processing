from abs_data import AbsData


class Data(AbsData):

    def __init__(self, identifier: str, content: str):
        self.__identifier = identifier
        self.__content = content

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def content(self) -> str:
        return self.__content
