from abc import ABC, abstractmethod


class CompressFileStrategy(ABC):
    @abstractmethod
    def compress(self, file: str):
        pass


class ZipCompress(CompressFileStrategy):
    def compress(self, file):
        print("Zip compressing ", file)


class XyzCompress(CompressFileStrategy):

    def compress(self, file):
        print("xyz compressing ", file)


class Compressor:
    def __init__(self, strategy: CompressFileStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def compress_file(self, file):
        self.strategy.compress(file)


if __name__ == "__main__":
    zip = ZipCompress()
    xyz = XyzCompress()
    compressor = Compressor(zip)
    compressor.compress_file("file.txt")
    compressor.set_strategy(xyz)
    compressor.compress_file("file2.txt")
