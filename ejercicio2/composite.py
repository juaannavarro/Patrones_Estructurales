from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import os

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
    def guardar(self, path):
        with open(os.path.join(path, self.nombre + '.' + self.tipo), 'w') as file:
            file.write(self.contenido)
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

    def __init__(self, nombre) -> None:
        self.nombre = nombre
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
class ProxyDocumento(Documento):
    """
    ProxyDocumento actúa como intermediario para la clase Documento.
    Controla el acceso y puede añadir funcionalidades adicionales como
    registro de acceso y verificación de permisos.
    """

    def __init__(self, documento_real: Documento) -> None:
        super().__init__(documento_real.nombre, documento_real.tipo, 
                         documento_real.tamaño, documento_real.contenido)
        self._documento_real = documento_real

    def request(self) -> None:
        if self.check_access():
            self._documento_real.operation()
            self.log_access()

    def check_access(self) -> bool:
        print(f"ProxyDocumento: Verificando acceso para {self.nombre}.")
        # Aquí iría la lógica para verificar permisos
        return True

    def log_access(self) -> None:
        print(f"ProxyDocumento: Registrando acceso a {self.nombre}.", end="")
class GestorDocumental:
    """
    GestorDocumental actúa como el punto central para gestionar documentos, enlaces y carpetas.
    """

    def __init__(self):
        self.raiz = Carpeta('raiz')

    def añadir_componente(self, componente: Component, carpeta: Carpeta = None):
        if carpeta is None:
            carpeta = self.raiz
        carpeta.add(componente)

    def eliminar_componente(self, componente: Component, carpeta: Carpeta = None):
        if carpeta is None:
            carpeta = self.raiz
        carpeta.remove(componente)

    def mostrar_estructura(self, componente: Component = None):
        if componente is None:
            componente = self.raiz
        print(componente.operation())
    def guardar_todos(self, path):
        for child in self.raiz._children:
            if isinstance(child, Documento):
                child.guardar(path)
            elif isinstance(child, Carpeta):
                new_path = os.path.join(path, child.nombre)
                os.makedirs(new_path, exist_ok=True)
                self._guardar_carpeta(child, new_path)

    def _guardar_carpeta(self, carpeta, path):
        for child in carpeta._children:
            if isinstance(child, Documento):
                child.guardar(path)
            elif isinstance(child, Carpeta):
                new_path = os.path.join(path, child.nombre)
                os.makedirs(new_path, exist_ok=True)
                self._guardar_carpeta(child, new_path)

if __name__ == "__main__":
    gestor = GestorDocumental()

    # Crear documentos y carpetas
    documento_simple = Documento("Informe", "txt", 1024, "Contenido del informe")
    documento_secreto = ProxyDocumento(Documento("InformeSecreto", "pdf", 2048, "Contenido confidencial"))
    carpeta_personal = Carpeta("Personal")

    # Añadir documentos y carpetas al gestor
    gestor.añadir_componente(documento_simple)
    gestor.añadir_componente(documento_secreto, carpeta_personal)
    gestor.añadir_componente(carpeta_personal)

    # Mostrar la estructura del gestor documental
    print("Estructura del Gestor Documental:")
    gestor.mostrar_estructura()

    # Acceder a un documento a través del proxy
    print("\nAcceso al Documento Secreto a través del Proxy:")
    documento_secreto.request()
    #guardar todos los documentos en una carpeta
    
    gestor.guardar_todos('ejercicio2')
    
    