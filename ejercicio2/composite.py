from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import os
import random
import string



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
                
def generar_nombre_aleatorio(longitud):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for i in range(longitud))

def generar_tipo_aleatorio():
    tipos = ['txt', 'pdf', 'doc', 'jpg']
    return random.choice(tipos)

def generar_contenido_aleatorio(palabras=50):
    palabras = [generar_nombre_aleatorio(random.randint(4, 10)) for _ in range(palabras)]
    return ' '.join(palabras)

def menu_principal(gestor):

    while True:
        print("\nGestor Documental")
        print("1. Crear documento aleatorio")
        print("2. Crear documento secreto aleatorio")
        print("3. Crear documento")
        print("4. Crear carpeta")
        print("5. Mostrar estructura")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = generar_nombre_aleatorio(10)
            tipo = generar_tipo_aleatorio()
            contenido = generar_contenido_aleatorio()
            documento = Documento(nombre, tipo, len(contenido), contenido)
            gestor.añadir_componente(documento)
            print(f"Documento {nombre}.{tipo} creado.")           
        elif opcion == '2':
            nombre = generar_nombre_aleatorio(10)
            tipo = generar_tipo_aleatorio()
            contenido = generar_contenido_aleatorio()
            documento = ProxyDocumento(Documento(nombre, tipo, len(contenido), contenido))
            gestor.añadir_componente(documento)
            print(f"Documento {nombre}.{tipo} creado.")           
        elif opcion == '3':           
            nombre = input("Ingrese el nombre del documento: ")
            tipo = input("Ingrese el tipo del documento: ")
            tamaño = input("Ingrese el tamaño del documento: ")
            contenido = input("Ingrese el contenido del documento: ")
            private = input("¿Es privado? (s/n): ")
            if private == 's':
                Documento_secreto = ProxyDocumento(Documento(nombre, tipo, tamaño, contenido))
                carpeta_personal = Carpeta("Personal")
                gestor.añadir_componente(Documento_secreto, carpeta_personal)
            else:               
                Documento_simple = Documento(nombre, tipo, tamaño, contenido)
                gestor.añadir_componente(Documento_simple)
            print(f"Documento {nombre}.{tipo} creado.")
        elif opcion == '4':
            nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
            carpeta = Carpeta(nombre_carpeta)
            gestor.añadir_componente(carpeta)
            print(f"Carpeta '{nombre_carpeta}' creada.")
        elif opcion == '5':
            gestor.mostrar_estructura()
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    gestor = GestorDocumental()

    
    # Crear documentos y carpetas
    documento_simple = Documento("Informe", "txt", 1024, "Contenido del informeeeee")
    documento_secreto = ProxyDocumento(Documento("InformeSecreto", "pdf", 2048, "Contenido Confidencial"))
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
    menu_principal(gestor)   
    gestor.guardar_todos('ejercicio2')
    
    