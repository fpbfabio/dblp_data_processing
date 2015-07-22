from abs_executor import AbsExecutor
from executor_factory import ExecutorFactory


class Executor(AbsExecutor):

    def __init__(self):
        self.__factory = ExecutorFactory()

    @property
    def factory(self):
        return self.__factory

    def execute(self):
        parser = self.factory.create_file_parser()
        serializer = self.factory.create_xml_serializer()
        data_list = parser.parse()
        serializer.serialize(data_list)


if __name__ == "__main__":
    executor = Executor()
    executor.execute()
