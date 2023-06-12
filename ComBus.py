from typing import Any, Dict, Type, Union
from typing_extensions import Self

# kanske ett registry pattern?


class ComBus:
    _registry: Dict[str, Type[Self]] = {}

    def __init_subclass__(cls, protocol: str):
        super().__init_subclass__()
        cls._registry[protocol] = cls

    def __new__(cls, bus: str, *args: Any, **kwargs: Any) -> Self:
        match bus:
            case "A":
                protocol = "A"
            case "B":
                protocol = "B"
            case _:
                raise ValueError("Invalid bus type")

        instance = super().__new__(cls._registry[protocol])
        return instance

    def communicate(self, message: str) -> str:
        # tests

        # communicate with bus using its protocol
        response = self._communicate(message)
        return response

    def _communicate(self, message: str) -> str:
        raise NotImplementedError


class BusA(ComBus, protocol="A"):
    def __init__(self, bus: str, *args: Any, **kwargs: Any):
        print("=====================================")
        print("BusA init called")
        print(f"{args=}, {kwargs=}")
        print("=====================================")
        assert bus == "A"
        super().__init__()
        self._bus = bus

    def _communicate(self, message: str) -> str:
        # communicate with bus A using its protocol
        print("Communicating with bus A")
        print(f"{message = }")
        print("Done communicating with bus A")


class BusB(ComBus, protocol="B"):
    def __init__(self, bus: str, *args: Any, **kwargs: Any):
        print("=====================================")
        print("BusB init called")
        print(f"{args=}, {kwargs=}")
        print("=====================================")
        assert bus == "B"
        super().__init__()
        self._bus = bus

    def _communicate(self, message: str) -> str:
        # communicate with bus B using its protocol
        print("Communicating with bus B")
        print(f"{message = }")
        print("Done communicating with bus B")


def communicate_with_bus(bus_type: str, message: str) -> str:
    if bus_type == "A":
        bus = ComBus(bus_type)
    elif bus_type == "B":
        bus = ComBus(bus_type)
    else:
        raise ValueError("Invalid bus type")

    return bus.communicate(message)


def main():
    communicate_with_bus("A", "Hello")
    communicate_with_bus("B", "Hello")
    bus = ComBus("A", "Hello", "World", key="value")


if __name__ == "__main__":
    main()
