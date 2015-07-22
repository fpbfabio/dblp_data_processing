from abs_file_parser import AbsFileParser
from abs_xml_serializer import AbsXmlSerializer
from abs_executor_factory import AbsExecutorFactory
from file_parser import FileParser
from xml_serializer import XmlSerializer


class ExecutorFactory(AbsExecutorFactory):
    def create_xml_serializer(self) -> AbsXmlSerializer:
        return XmlSerializer()

    def create_file_parser(self) -> AbsFileParser:
        return FileParser()
