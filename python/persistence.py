from const import *
from utils import Utils
from document import Document
from dblp import DBLP


class Persistence:

	@staticmethod
	def document_list_to_solr_xml(document_list, path):
		with open(path, WRITE_MODE) as archive:
			archive.write(XML_HEADER)
			archive.write(SOLR_XML_ADD_OPEN_TAG + EOL)
			for document in document_list:
				archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_OPEN_TAG + EOL)
				for inner_list in document.content_list:
					field_name = inner_list[DOCUMENT_FIELD_NAME_INDEX]
					field_value = inner_list[DOCUMENT_FIELD_VALUE_INDEX]
					field_value = Utils.string_replace(CDATA_CLOSE_TAG, "]]" + CDATA_CLOSE_TAG + CDATA_OPEN_TAG + ">", field_value)
					field_open_tag = Utils.string_replace(REPLACE_MASK, field_name, SOLR_XML_FIELD_OPEN_TAG)
					archive.write(2 * TAB_SPACE + field_open_tag + CDATA_OPEN_TAG + field_value + CDATA_CLOSE_TAG + SOLR_XML_FIELD_CLOSE_TAG + EOL)
				archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_CLOSE_TAG + EOL)
			archive.write(SOLR_XML_ADD_CLOSE_TAG + EOL)

	@staticmethod
	def get_document_list_from_file(path):
		document_list = []
		with open(path, READ_MODE) as archive:
			document = Document(EMPTY_STRING)
			document.add_field(DBLP.TITLE_FIELD_NAME, EMPTY_STRING)
			for line in archive:
				key_beginning_index = line.find(DBLP.KEY_MARK) + len(DBLP.KEY_MARK) + 1
				if(key_beginning_index != len(DBLP.KEY_MARK)):
					key_end_index = min(line.find("\">"), line.find("\" publtype"))
					key = line[key_beginning_index:key_end_index]
					document.identifier = key
				title_beginning_index = line.find(DBLP.TITLE_TAG_BEGINNING) + len(DBLP.TITLE_TAG_BEGINNING)
				if(title_beginning_index != len(DBLP.TITLE_TAG_BEGINNING) - 1):
					title_end_index = line.find(DBLP.TITLE_TAG_END)
					title = line[title_beginning_index:title_end_index]
					document.set_field(DBLP.TITLE_FIELD_NAME, title)
					document_list.append(document)
					document = Document(EMPTY_STRING)
					document.add_field(DBLP.TITLE_FIELD_NAME, EMPTY_STRING)
		return document_list