from composite import *

import unittest


class TestDocumento(unittest.TestCase):

    def setUp(self):
        self.doc = Documento("TestDoc", "txt", 100, "Este es el contenido")

    def test_documento_creation(self):
        self.assertEqual(self.doc.nombre, "TestDoc")
        self.assertEqual(self.doc.tipo, "txt")
        self.assertEqual(self.doc.tamaño, 100)
        self.assertEqual(self.doc.contenido, "Este es el contenido")

    def test_modificar_documento(self):
        self.doc.modificar_contenido("Contenido modificado")
        self.assertEqual(self.doc.contenido, "Contenido modificado")
        self.assertEqual(self.doc.tamaño, len("Contenido modificado"))

class TestCarpeta(unittest.TestCase):

    def setUp(self):
        self.carpeta = Carpeta("CarpetaTest")
        self.doc1 = Documento("Doc1", "txt", 100, "Contenido 1")
        self.doc2 = Documento("Doc2", "txt", 200, "Contenido 2")

    def test_añadir_documento(self):
        self.carpeta.add(self.doc1)
        self.assertIn(self.doc1, self.carpeta._children)

    def test_eliminar_documento(self):
        self.carpeta.add(self.doc1)
        self.carpeta.remove(self.doc1)
        self.assertNotIn(self.doc1, self.carpeta._children)

class TestGestorDocumental(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorDocumental()
        self.doc = Documento("TestDoc", "txt", 100, "Contenido del doc")
        self.carpeta = Carpeta("CarpetaTest")

    def test_añadir_documento_a_gestor(self):
        self.gestor.añadir_componente(self.doc, self.carpeta)
        self.assertIn(self.doc, self.carpeta._children)






def menu_principal(gestor, usuario_actual=Usuario("Admin", True)):

    
    while True:
        print("\nGestor Documental")
        print("1. Crear documento aleatorio")
        if usuario_actual.es_admin:
            print("2. Crear documento secreto aleatorio")
        print("3. Crear documento")
        print("4. Crear carpeta")
        print("5. Mostrar estructura")
        print(f"6. Cambiar usuario (actualmente: {'Admin' if usuario_actual.es_admin else 'User'})")
        print("7. Salir")
        print("8. Modificar documento")
        print("9. Eliminar documento o carpeta")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = generar_nombre_aleatorio(10)
            tipo = generar_tipo_aleatorio()
            contenido = generar_contenido_aleatorio()
            documento = Documento(nombre, tipo, len(contenido), contenido)
            carpeta_global = Carpeta("Global")
            gestor.añadir_componente(documento, carpeta_global)
            gestor.añadir_componente(carpeta_global)
            print(f"Documento {nombre}.{tipo} creado.")           
        elif opcion == '2' and usuario_actual.es_admin:
            nombre = generar_nombre_aleatorio(10)
            tipo = generar_tipo_aleatorio()
            contenido = generar_contenido_aleatorio()
            documento = ProxyDocumento(Documento(nombre, tipo, len(contenido), contenido))
            carpeta_personal = Carpeta("Personal")
            gestor.añadir_componente(documento, carpeta_personal)
            gestor.añadir_componente(carpeta_personal)
            print(f"Documento secreto {nombre}.{tipo} creado.")           
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
                gestor.añadir_componente(carpeta_personal)
            else:               
                Documento_simple = Documento(nombre, tipo, tamaño, contenido)
            carpeta_global = Carpeta("Global")
            gestor.añadir_componente(Documento_simple, carpeta_global)
            gestor.añadir_componente(carpeta_global)
            print(f"Documento {nombre}.{tipo} creado.")
        elif opcion == '4':
            nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
            carpeta = Carpeta(nombre_carpeta)
            gestor.añadir_componente(carpeta)
            print(f"Carpeta '{nombre_carpeta}' creada.")
        elif opcion == '5':
            gestor.mostrar_estructura()
        elif opcion == '6':
            usuario_actual.es_admin = not usuario_actual.es_admin
            print("Cambiado a usuario administrador." if usuario_actual.es_admin else "Cambiado a usuario normal.")
        elif opcion == '7':
            break       
        elif opcion == '8':
            nombre_documento = input("Ingrese el nombre del documento a modificar: ")
            nuevo_contenido = input("Ingrese el nuevo contenido del documento: ")
            gestor.modificar_documento(nombre_documento, nuevo_contenido)

        elif opcion == '9':
            nombre_componente = input("Ingrese el nombre del documento o carpeta a eliminar: ")
            gestor.eliminar_componente(nombre_componente)    
        else:
            print("Opción no válida, intente nuevamente.")

        gestor.guardar_todos('ejercicio2')

    

    
if __name__ == '__main__':
    unittest.main()