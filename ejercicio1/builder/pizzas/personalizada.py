from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from pizzeria import Pizzeria

class ConstructorPersonalizada(Pizzeria):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Personalizada()

    @property
    def product(self) -> Personalizada:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> None:
        return self._product

    def masa(self, tipo: str) -> None:
        self._product.add(f"Masa {tipo}")

    def salsa_base(self, tipo: str) -> None:
        self._product.add(f"Salsa: {tipo}")

    def ingredientes(self, ingredientes: List[str]) -> None:
        for ingrediente in ingredientes:
            self._product.add(f"Ingrediente: {ingrediente}")

    def coccion(self, tipo: str) -> None:
        self._product.add(f"Cocción: {tipo}")

    def presentacion(self, tipo: str) -> None:
        self._product.add(f"Presentación: {tipo}")

    def maridaje(self, tipo: str) -> None:
        self._product.add(f"Maridaje: {tipo}")

    def extras(self, extras: List[str]) -> None:
        for extra in extras:
            self._product.add(f"Extra: {extra}")




class Personalizada():
    def __init__(self) -> None:
        self.parts = []
        self.base_price = 7
    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        return f"Partes de la pizza: {', '.join(self.parts)}"

    def calculate_price(self) -> None:
        extra_cost = 1  # Costo adicional por cada extra
        number_of_extras = sum("Extra:" in part for part in self.parts)
        return self.base_price + number_of_extras * extra_cost