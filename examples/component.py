from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self, *args, **kwargs) -> None:  # type: ignore
        raise NotImplementedError
