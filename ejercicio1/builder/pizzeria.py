from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Pizzeria(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass
    @abstractmethod
    def masa(self, tipo: str) -> None:
        pass

    @abstractmethod
    def salsa_base(self, tipo: str) -> None:
        pass

    @abstractmethod
    def ingredientes(self, ingredientes: List[str]) -> None:
        pass

    @abstractmethod
    def coccion(self, tipo: str) -> None:
        pass

    @abstractmethod
    def presentacion(self, tipo: str) -> None:
        pass

    @abstractmethod
    def maridaje(self, tipo: str) -> None:
        pass

    @abstractmethod
    def extras(self, extras: List[str]) -> None:
        pass
