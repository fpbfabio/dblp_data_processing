import sys
from document import Document
from persistence import Persistence
from const import XML_FILE_EXTENSION


document_list = Persistence.get_document_list_from_file(sys.argv[1])
Persistence.document_list_to_solr_xml(document_list, sys.argv[2])