from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    """
    La clase base Component declara operaciones comunes tanto para objetos
    simples como para objetos complejos de una composición.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Documento(Component):
    """
    Clase Documento representa documentos individuales en el sistema.
    """

    def __init__(self, nombre, tipo, tamaño, contenido):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.contenido = contenido

    def operation(self) -> str:
        return f"Documento({self.nombre}, {self.tipo})"

class Enlace(Component):
    """
    Clase Enlace representa un enlace a otro componente del sistema.
    """

    def __init__(self, referencia):
        self.referencia = referencia

    def operation(self) -> str:
        return f"Enlace({self.referencia.operation()})"

class Carpeta(Component):
    """
    Clase Carpeta representa una colección de Componentes.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Carpeta({'+'.join(results)})"

def client_code(component: Component) -> None:
    print(f"RESULTADO: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULTADO: {component1.operation()}", end="")

if __name__ == "__main__":
    # Uso de la clase Documento
    documento_simple = Documento("Informe", "txt", 1024, "Contenido del informe")
    print("Cliente: Tengo un documento simple:")
    client_code(documento_simple)
    print("\n")

    # Uso de la clase Carpeta
    carpeta = Carpeta()
    carpeta.add(documento_simple)
    carpeta.add(Enlace(documento_simple))

    print("Cliente: Ahora tengo una carpeta:")
    client_code(carpeta)
    print("\n")

