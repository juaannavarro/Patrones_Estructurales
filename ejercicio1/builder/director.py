from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from pizzeria import Pizzeria
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Pizzeria:
        return self._builder

    @builder.setter
    def builder(self, builder: Pizzeria) -> None:
        self._builder = builder

    def build_personalizada(self, masa: str, salsa: str, ingredientes: List[str], coccion: str, presentacion: str, maridaje: str, extras: List[str]) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base(salsa)
        self.builder.ingredientes(ingredientes)
        self.builder.coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridaje(maridaje)
        self.builder.extras(extras)
        
    def build_jamonyqueso(self, masa: str, coccion: str, presentacion: str, maridaje: str, extras: List[str]) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridaje(maridaje)
        self.builder.extras(extras)
        
    def build_barbacoa(self, masa: str, coccion: str, presentacion: str, maridaje: str, extras: List[str]) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridaje(maridaje)
        self.builder.extras(extras)
        
    def build_cuatroQuesos(self, masa: str, coccion: str, presentacion: str, maridaje: str, extras: List[str]) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridaje(maridaje)
        self.builder.extras(extras)

    def build_infantil(self, extras: List[str]) -> None:
        self.builder.masa()
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridaje()
        self.builder.extras(extras)
    


    
    




    
    

