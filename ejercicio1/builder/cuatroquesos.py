from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from pizzeria import Pizzeria

class ConstructorcuatroQuesos(Pizzeria):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = cuatroQuesos()

    @property
    def product(self) -> cuatroQuesos:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> None:
        return self._product

    def masa(self, tipo: str) -> None:
        self._product.add(f"Masa {tipo}")

    def salsa_base(self) -> None:
        self._product.add("Salsa: Tomate")


    def ingredientes(self) -> None:
        quesos = ["Mozzarella", "Cheddar", "Parmesano", "Gorgonzola"]
        for queso in quesos:
            self._product.add(f"Ingrediente: Queso {queso}")

    def coccion(self, tipo: str) -> None:
        self._product.add(f"Cocción: {tipo}")

    def presentacion(self, tipo: str) -> None:
        self._product.add(f"Presentación: {tipo}")

    def maridaje(self, tipo: str) -> None:
        self._product.add(f"Maridaje: {tipo}")

    def extras(self, extras: List[str]) -> None:
        for extra in extras:
            self._product.add(f"Extra: {extra}")




class cuatroQuesos():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Personalizada: {', '.join(self.parts)}", end="")