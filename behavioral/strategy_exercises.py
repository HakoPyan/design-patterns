import csv
from abc import ABC, abstractmethod
from typing import Any


# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> list[dict[str, Any]]:
        pass


# Step 2: Implement the file parsers
class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict[str, Any]]:
        pass


class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict[str, Any]]:
        pass


class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict[str, Any]]:
        pass


# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        self._file_parser = file_parser

    def read_file(self, file_path: str) -> list[dict[str, Any]]:
        return self._file_parser.parse_file(file_path)


# Step 4: Test your implementation
if __name__ == "__main__":
    reader = FileReader(CSVParser())

    data = reader.read_file("sample.csv")
    print(data)
