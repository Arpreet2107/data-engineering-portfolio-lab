# ============================================
# COMPLETE OOP IN PYTHON (DATA ENGINEERING STYLE)
# ============================================

from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from datetime import datetime


# ============================================
# LOGGER (Singleton Pattern)
# ============================================

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"[{datetime.now()}] {message}")


# ============================================
# CONFIG USING CLASSMETHOD & STATICMETHOD
# ============================================

class Config:
    _env = "DEV"

    @classmethod
    def get_env(cls):
        return cls._env

    @staticmethod
    def validate_env(env):
        return env in ["DEV", "PROD"]


# ============================================
# DATACLASS (FOR STRUCTURED DATA)
# ============================================

@dataclass
class Record:
    id: int
    level: str
    message: str


# ============================================
# ABSTRACT BASE CLASS (ABSTRACTION)
# ============================================

class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass


class DataSink(ABC):
    @abstractmethod
    def write(self, data):
        pass


class Transformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass


# ============================================
# CONCRETE DATA SOURCES (INHERITANCE)
# ============================================

class FileSource(DataSource):
    def __init__(self, file_path):
        self._file_path = file_path  # encapsulation

    def read(self):
        with open(self._file_path, 'r') as f:
            return f.readlines()


class APISource(DataSource):
    def read(self):
        # simulate API response
        return [
            '{"id":1,"level":"error","message":"fail"}',
            '{"id":2,"level":"info","message":"success"}'
        ]


# ============================================
# TRANSFORMERS (STRATEGY PATTERN)
# ============================================

class JSONTransformer(Transformer):
    def transform(self, data):
        result = []
        for line in data:
            try:
                result.append(json.loads(line))
            except:
                continue
        return result


class UpperCaseTransformer(Transformer):
    def transform(self, data):
        return [str(d).upper() for d in data]


# ============================================
# FILTER CLASS (COMPOSITION)
# ============================================

class ErrorFilter:
    def apply(self, data):
        return [d for d in data if "error" in d.get("level", "").lower()]


# ============================================
# DATA SINKS
# ============================================

class FileSink(DataSink):
    def __init__(self, file_path):
        self._file_path = file_path

    def write(self, data):
        with open(self._file_path, 'w') as f:
            json.dump(data, f, indent=2)


class ConsoleSink(DataSink):
    def write(self, data):
        print("OUTPUT:", data)


# ============================================
# FACTORY PATTERN
# ============================================

class SourceFactory:
    @staticmethod
    def get_source(source_type, path=None):
        if source_type == "file":
            return FileSource(path)
        elif source_type == "api":
            return APISource()
        else:
            raise ValueError("Invalid source type")


# ============================================
# MAIN PIPELINE (COMPOSITION + DI)
# ============================================

class Pipeline:
    def __init__(self, source: DataSource, transformer: Transformer, sink: DataSink):
        self.source = source
        self.transformer = transformer
        self.sink = sink
        self.logger = Logger()
        self.filter = ErrorFilter()

    def run(self):
        self.logger.log("Pipeline started")

        raw_data = self.source.read()
        self.logger.log(f"Read {len(raw_data)} records")

        transformed = self.transformer.transform(raw_data)
        self.logger.log(f"Transformed {len(transformed)} records")

        filtered = self.filter.apply(transformed)
        self.logger.log(f"Filtered {len(filtered)} records")

        self.sink.write(filtered)

        self.logger.log("Pipeline completed")


# ============================================
# ENCAPSULATION USING PROPERTY
# ============================================

class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# ============================================
# OPERATOR OVERLOADING (DUNDER METHODS)
# ============================================

class Data:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Data({self.value})"

    def __add__(self, other):
        return Data(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value


# ============================================
# POLYMORPHISM DEMO
# ============================================

def run_loader(loader):
    loader.load()


class CSVLoader:
    def load(self):
        print("Loading CSV")


class JSONLoader:
    def load(self):
        print("Loading JSON")


# ============================================
# MULTIPLE INHERITANCE + MRO
# ============================================

class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":

    # Factory usage
    source = SourceFactory.get_source("api")

    # Strategy pattern
    transformer = JSONTransformer()

    # Sink
    sink = ConsoleSink()

    # Dependency Injection into Pipeline
    pipeline = Pipeline(source, transformer, sink)
    pipeline.run()

    # Property demo
    user = User(25)
    user.age = 30

    # Operator overloading
    d1 = Data(10)
    d2 = Data(20)
    print(d1 + d2)

    # Polymorphism
    run_loader(CSVLoader())
    run_loader(JSONLoader())

    # MRO check
    print(C.__mro__)