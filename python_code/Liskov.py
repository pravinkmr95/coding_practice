from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, no_of_wheel):
        self._no_of_wheel = no_of_wheel

    @abstractmethod
    def number_of_wheel(self):
        pass

    def has_engine(self):
        return True


class EngineVehicle(Vehicle):
    def __init__(self, wh):
        super().__init__(wh)

    def number_of_wheel(self):
        return self._no_of_wheel


if __name__ == "__main__":
    obj = EngineVehicle(2)
    print(obj.number_of_wheel())
    # print(obj.has_engine())
    print(type(obj) is Vehicle)
