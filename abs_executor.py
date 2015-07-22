""""
This is the module that provides an abstract interface for a
class used to execute the code for convert the dblp files into xml
files suitable to be submitted to Apache Solr using the post.jar tool.
"""

from abc import ABCMeta, abstractmethod


class AbsExecutor(metaclass=ABCMeta):
    """
    Class used to execute the program.
    """
    @property
    @abstractmethod
    def factory(self):
        """
        Object of type AbsExecutorFactory.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Executes the code.
        """
        pass
