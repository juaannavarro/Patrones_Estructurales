from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from pizzeria import Pizzeria

class ConstructorInfantil:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = infantil()

    @property
    def product(self) -> infantil:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> None:
        return self._product

    def masa(self) -> None:
        self._product.add("Masa fina ")

    def salsa_base(self) -> None:
        self._product.add("Salsa: Tomate")


    def ingredientes(self) -> None:     
        self._product.add("Ingrediente: Jamón")
        self._product.add("Ingrediente: Queso")


    def coccion(self) -> None:
        self._product.add("Cocción: Horno")

    def presentacion(self) -> None:
        self._product.add("Presentación: Cortada en 4")

    def maridaje(self, ) -> None:
        self._product.add("Maridaje: Aceite de oliva")

    def extras(self, extras: List[str]) -> None:
        for extra in extras:
            self._product.add(f"Extra: {extra}")
            
class infantil():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        return f"Partes de la pizza: {', '.join(self.parts)}"