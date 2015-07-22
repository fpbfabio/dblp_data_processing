import os

from abs_data import AbsData
from abs_xml_serializer import AbsXmlSerializer


class XmlSerializer(AbsXmlSerializer):
    FILE_PERMISSION = "w"
    FILE_PATH = ""

    def serialize(self, data_list: [AbsData]) -> None:
        with open(XmlSerializer.FILE_PATH, XmlSerializer.FILE_PERMISSION) as archive:
            archive.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>" + os.linesep)
            archive.write("<add>" + os.linesep)
            for data in data_list:
                archive.write("\t<doc>" + os.linesep)
                identifier = data.identifier.replace("]]>", "]]]]><![CDATA[>")
                archive.write("\t\t<field name=\"id\"><![CDATA[" + identifier + "]]></field>" + os.linesep)
                content = data.content.replace("]]>", "]]]]><![CDATA[>")
                archive.write("\t\t<field name=\"text\"><![CDATA[" + content + "]]></field>" + os.linesep)
                archive.write("\t</doc>" + os.linesep)
            archive.write("</add>" + os.linesep)
