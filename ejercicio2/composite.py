from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import os
import random
import string

import unittest


class TestDocumento(unittest.TestCase):

    def test_crear_documento(self):
        doc = Documento("TestDoc", "txt", 100, "Este es el contenido")
        self.assertEqual(doc.nombre, "TestDoc")
        self.assertEqual(doc.tipo, "txt")
        self.assertEqual(doc.tamaño, 100)
        self.assertEqual(doc.contenido, "Este es el contenido")

    def test_modificar_documento(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido original")
        doc.modificar_contenido("Contenido nuevo")
        self.assertEqual(doc.contenido, "Contenido nuevo")
        self.assertEqual(doc.tamaño, len("Contenido nuevo"))
        
    def test_guardar_documento(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        doc.guardar(os.path.dirname(os.path.abspath(__file__)))
        ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), doc.nombre + '.' + doc.tipo)
        self.assertTrue(os.path.isfile(ruta_archivo))
        with open(ruta_archivo, 'r') as file:
            contenido_archivo = file.read()
        self.assertEqual(contenido_archivo, doc.contenido)
        os.remove(ruta_archivo)
        
    def test_crear_enlace(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        enlace = Enlace(doc)
        self.assertEqual(enlace.referencia, doc)
    
    def test_crear_carpeta(self):
        carpeta = Carpeta("TestCarpeta")
        self.assertEqual(carpeta.nombre, "TestCarpeta")
        self.assertEqual(carpeta._children, [])
        
    def test_añadir_componente(self):
        carpeta = Carpeta("TestCarpeta")
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        carpeta.add(doc)
        self.assertEqual(carpeta._children, [doc])
        self.assertEqual(doc.parent, carpeta)
        
    def test_remover_componente(self):
        carpeta = Carpeta("TestCarpeta")
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        carpeta.add(doc)
        carpeta.remove(doc)
        self.assertEqual(carpeta._children, [])
        self.assertIsNone(doc.parent)
        
    def test_es_composite(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        self.assertFalse(doc.is_composite())
        carpeta = Carpeta("TestCarpeta")
        self.assertTrue(carpeta.is_composite())
        
    def test_mostrar_estructura(self):
        carpeta = Carpeta("TestCarpeta")
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        carpeta.add(doc)
        self.assertEqual(carpeta.operation(), "Carpeta(Documento(TestDoc, txt))")
    
    def test_proxy_documento(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        proxy = ProxyDocumento(doc)
        self.assertEqual(proxy.nombre, "TestDoc")
        self.assertEqual(proxy.tipo, "txt")
        self.assertEqual(proxy.tamaño, 100)
        self.assertEqual(proxy.contenido, "Contenido")
        self.assertEqual(proxy._documento_real, doc)
    
    def test_proxy_documento_request(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        proxy = ProxyDocumento(doc)
        usuario = Usuario("TestUser", True)
        proxy.request(usuario)
        self.assertEqual(proxy.nombre, "TestDoc")
        self.assertEqual(proxy.tipo, "txt")
        self.assertEqual(proxy.tamaño, 100)
        self.assertEqual(proxy.contenido, "Contenido")
        self.assertEqual(proxy._documento_real, doc)
    
    def test_proxy_documento_request_denegado(self):
        doc = Documento("TestDoc", "txt", 100, "Contenido")
        proxy = ProxyDocumento(doc)
        usuario = Usuario("TestUser", False)
        proxy.request(usuario)
        self.assertEqual(proxy.nombre, "TestDoc")
        self.assertEqual(proxy.tipo, "txt")
        self.assertEqual(proxy.tamaño, 100)
        self.assertEqual(proxy.contenido, "Contenido")
        self.assertEqual(proxy._documento_real, doc)
    
    def test_gestor_documental(self):
        gestor = GestorDocumental()
        self.assertEqual(gestor.raiz.nombre, "raiz")
        self.assertEqual(gestor.raiz._children, [])
        
class Component(ABC):


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
            
    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        self.tamaño = len(nuevo_contenido)
        self.guardar(os.path.dirname(os.path.abspath(__file__)))
class Enlace(Component):


    def __init__(self, referencia):
        self.referencia = referencia

    def operation(self) -> str:
        return f"Enlace({self.referencia.operation()})"

class Carpeta(Component):


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
    
class Usuario:
    def __init__(self, nombre, es_admin):
        self.nombre = nombre
        self.es_admin = es_admin  # True para administradores, False para usuarios normales


class ProxyDocumento(Documento):

    def __init__(self, documento_real: Documento) -> None:
        super().__init__(documento_real.nombre, documento_real.tipo, 
                         documento_real.tamaño, documento_real.contenido)
        self._documento_real = documento_real
    def request(self, usuario: Usuario) -> None:
        if self.check_access(usuario) and usuario.es_admin:
            self._documento_real.operation()
            self.log_access(usuario)
        else:
            print(f"Acceso denegado para el usuario: {usuario.nombre}")

    def check_access(self, usuario: Usuario) -> bool:
        return usuario.es_admin  # Solo permitir acceso si el usuario es administrador

    def log_access(self, usuario: Usuario) -> None:
        print(f"Acceso registrado: {usuario.nombre} accedió a {self.nombre}")



class GestorDocumental:

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
    def modificar_documento(self, nombre_documento, nuevo_contenido, carpeta: Carpeta = None):
        carpeta_destino = carpeta if carpeta is not None else self.raiz
        documento_a_modificar = self._buscar_documento(carpeta_destino, nombre_documento)
        if documento_a_modificar:
            documento_a_modificar.modificar_contenido(nuevo_contenido)
            print(f"Documento '{nombre_documento}' modificado.")
        else:
            print(f"No se encontró el documento: {nombre_documento}")

    def _buscar_documento(self, carpeta, nombre_documento):
        for componente in carpeta._children:
            if isinstance(componente, Documento) and componente.nombre == nombre_documento:
                return componente
            elif isinstance(componente, Carpeta):
                resultado = self._buscar_documento(componente, nombre_documento)
                if resultado:
                    return resultado
        return None
    

    def eliminar_componente(self, nombre_componente, carpeta: Carpeta = None):
        carpeta_destino = carpeta if carpeta is not None else self.raiz
        componente_a_eliminar = self._buscar_componente(carpeta_destino, nombre_componente)
        if componente_a_eliminar:
            carpeta_destino.remove(componente_a_eliminar)
            if isinstance(componente_a_eliminar, Documento):
                self._eliminar_archivo(componente_a_eliminar)
            elif isinstance(componente_a_eliminar, Carpeta):
                self._eliminar_carpeta_recursivamente(componente_a_eliminar, os.path.join(os.path.dirname(os.path.abspath(__file__)), componente_a_eliminar.nombre))
            print(f"Componente '{nombre_componente}' eliminado.")
        else:
            print(f"No se encontró el componente: {nombre_componente}")

    def _eliminar_carpeta_recursivamente(self, carpeta, ruta_carpeta):
        for hijo in carpeta._children:
            if isinstance(hijo, Documento):
                self._eliminar_archivo(hijo)
            elif isinstance(hijo, Carpeta):
                sub_ruta_carpeta = os.path.join(ruta_carpeta, hijo.nombre)
                self._eliminar_carpeta_recursivamente(hijo, sub_ruta_carpeta)
        if os.path.isdir(ruta_carpeta):
            os.rmdir(ruta_carpeta)

    def _eliminar_archivo(self, documento: Documento):
        ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), documento.nombre + '.' + documento.tipo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

    def _buscar_componente(self, carpeta, nombre_componente):
        for componente in carpeta._children:
            if (isinstance(componente, Documento) or isinstance(componente, Carpeta)) and componente.nombre == nombre_componente:
                return componente
            elif isinstance(componente, Carpeta):
                resultado = self._buscar_componente(componente, nombre_componente)
                if resultado:
                    return resultado
        return None         
def generar_nombre_aleatorio(longitud):
    letras = string.ascii_letters
    return ''.join(random.choice(letras) for i in range(longitud))

def generar_tipo_aleatorio():
    tipos = ['txt', 'pdf', 'doc', 'jpg']
    return random.choice(tipos)

def generar_contenido_aleatorio(palabras=50):
    palabras = [generar_nombre_aleatorio(random.randint(4, 10)) for _ in range(palabras)]
    return ' '.join(palabras)

if __name__ == '__main__':
    unittest.main()