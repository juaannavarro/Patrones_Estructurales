import os
import csv
from pizzas.jamonyqueso import jamonyqueso, Constructorjamonyqueso
from pizzas.cuatroquesos import cuatroQuesos, ConstructorcuatroQuesos
from director import Director
from pizzas.personalizada import Personalizada, ConstructorPersonalizada
from pizzeria import Pizzeria
from pizzas.barbacoa import Barbacoa, ConstructorBarbacoa
from usuario import UsuarioBuilder, UsuarioDirector
import collections


class Menu(Pizzeria):

    def Menu():
        
        print("Bienvenido a la pizzeria")
        usuario_builder = UsuarioBuilder()
        usuario_director = UsuarioDirector(usuario_builder)
        usuario_director.crear_usuario("","","","")
        usuario = usuario_director.get_usuario()
        print("Por favor, ingrese sus datos")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        telefono = input("Telefono: ")
        usuario_director.crear_usuario(nombre, apellido, email, telefono)
        usuario = usuario_director.get_usuario()
        print(usuario)
        print("Elija el tipo de pizza:")
        print("1. Jamón y queso")
        print("2. Cuatro quesos")
        print("3. Barbacoa")
        print("4. Personalizada")
        pizza_opcion = input("Elija una opción: ")
        pizza_seleccionada = []

        if pizza_opcion == "1":
            pizza_seleccionada = ["Jamón y Queso"]
            director = Director()
            builder = Constructorjamonyqueso()
            director.builder = builder
            
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"

            print("\nElija el tipo de coccion:")
            print("1. Horno")
            print("2. Microondas")
            coccion_opcion = input("Elija una opción: ")
            coccion_seleccionada = "horno" if coccion_opcion == "1" else "microondas"
            
            print("\nElija el tipo de presentación:")
            print("1. Caja")
            print("2. Plato")
            presentacion_opcion = input("Elija una opción: ")
            presentacion_seleccionada = "caja" if presentacion_opcion == "1" else "plato"
        
            print("\nElija el tipo de maridaje:")
            print("1. Vino tinto")
            print("2. Cerveza")
            maridaje_opcion = input("Elija una opción: ")
            maridaje_seleccionado = "vino tinto" if maridaje_opcion == "1" else "cerveza"
            
            print("\nElija los extras:")
            print("1. Aceitunas")
            print("2. Queso extra")
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Aceitunas"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Queso extra"]
            elif extras_opcion == "3":
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
                
            director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "2":
            pizza_seleccionada = ["Cuatro quesos"]
            director = Director()
            builder = ConstructorcuatroQuesos()
            director.builder = builder
        
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"
        
            print("\nElija el tipo de coccion:")
            print("1. Horno")
            print("2. Microondas")
            coccion_opcion = input("Elija una opción: ")
            coccion_seleccionada = "horno" if coccion_opcion == "1" else "microondas"
        
            print("\nElija el tipo de presentación:")
            print("1. Caja")
            print("2. Plato")
            presentacion_opcion = input("Elija una opción: ")
            presentacion_seleccionada = "caja" if presentacion_opcion == "1" else "plato"
        
            print("\nElija el tipo de maridaje:")
            print("1. Vino tinto")
            print("2. Cerveza")
            maridaje_opcion = input("Elija una opción: ")
            maridaje_seleccionado = "vino tinto" if maridaje_opcion == "1" else "cerveza"
        
            print("\nElija los extras:")
            print("1. Aceitunas")
            print("2. Prosciutto")
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Aceitunas"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Prosciutto"]
            elif extras_opcion == "3": 
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
            
            director.build_cuatroQuesos(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "3":
            pizza_seleccionada = ["Barbacoa"]
            director = Director()
            builder = ConstructorBarbacoa()
            director.builder = builder
        
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"
        
            print("\nElija el tipo de coccion:")
            print("1. Horno")
            print("2. Microondas")
            coccion_opcion = input("Elija una opción: ")
            coccion_seleccionada = "horno" if coccion_opcion == "1" else "microondas"
        
            print("\nElija el tipo de presentación:")
            print("1. Caja")
            print("2. Plato")
            presentacion_opcion = input("Elija una opción: ")
            presentacion_seleccionada = "caja" if presentacion_opcion == "1" else "plato"
        
            print("\nElija el tipo de maridaje:")
            print("1. Vino tinto")
            print("2. Cerveza")
            maridaje_opcion = input("Elija una opción: ")
            maridaje_seleccionado = "vino tinto" if maridaje_opcion == "1" else "cerveza"
        
            print("\nElija los extras:")
            print("1. Borde rellenos de queso")
            print("2. Maíz")
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Borde rellenos de queso"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Maíz"]
            elif extras_opcion == "3":
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
            
            director.build_barbacoa(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "4":
                pizza_seleccionada = ["Personalizada"]
                director = Director()
                builder = ConstructorPersonalizada()
                director.builder = builder
                print("Elija el tipo de masa:")
                print("1. Masa gruesa")
                print("2. Masa fina")
                masa_opcion = input("Elija una opción: ")
                masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"

                print("\nElija el tipo de salsa:")
                print("1. Salsa de tomate")
                print("2. Salsa BBQ")
                salsa_opcion = input("Elija una opción: ")
                salsa_seleccionada = "tomate" if salsa_opcion == "1" else "BBQ"

                print("\nElija los ingredientes:")
                print("1. Jamón")
                print("2. Queso")
                print("3. Champiñones")
                print("4. Cebolla")
                print("5. Pimiento")
                print("6. Tomate")
                print("7. Piña")
                print("8. Pollo")
                print("9. Carne picada")
                print("10. Bacon")
                ingredientes_opcion = None
                ingredientes_seleccionados = []
                while ingredientes_opcion != "0":
                    ingredientes_opcion = input("Elija una opción o presione 0 para finalizar: ")
                    if ingredientes_opcion == "1":
                        ingredientes_seleccionados.append("Jamón")
                    elif ingredientes_opcion == "2":
                        ingredientes_seleccionados.append("Queso")
                    elif ingredientes_opcion == "3":
                        ingredientes_seleccionados.append("Champiñones")
                    elif ingredientes_opcion == "4":
                        ingredientes_seleccionados.append("Cebolla")
                    elif ingredientes_opcion == "5":
                        ingredientes_seleccionados.append("Pimiento")
                    elif ingredientes_opcion == "6":
                        ingredientes_seleccionados.append("Tomate")
                    elif ingredientes_opcion == "7":
                        ingredientes_seleccionados.append("Piña")
                    elif ingredientes_opcion == "8":
                        ingredientes_seleccionados.append("Pollo")
                    elif ingredientes_opcion == "9":
                        ingredientes_seleccionados.append("Carne picada")
                    elif ingredientes_opcion == "10":
                        ingredientes_seleccionados.append("Bacon")
                    elif ingredientes_opcion == "0":
                        print("Finalizando selección de ingredientes.")
                    else:
                        print("Opción no válida. Por favor, intente de nuevo.")
                        
                print("\nElija el tipo de cocción:")
                print("1. Horno")
                print("2. Microondas")
                coccion_opcion = input("Elija una opción: ")
                coccion_seleccionada = "horno" if coccion_opcion == "1" else "microondas"

                print("\nElija el tipo de presentación:")
                print("1. Caja")
                print("2. Plato")
                presentacion_opcion = input("Elija una opción: ")
                presentacion_seleccionada = "caja" if presentacion_opcion == "1" else "plato"

                print("\nElija el tipo de maridaje:")
                print("1. Vino tinto")
                print("2. Cerveza")
                maridaje_opcion = input("Elija una opción: ")
                maridaje_seleccionado = "vino tinto" if maridaje_opcion == "1" else "cerveza"
                
                print("\nElija los extras:")
                print("1. Cebolla caramelizada")
                print("2. Queso extra")
                print("3. Borde relleno de queso")
                print("4. Aceitunas")
                print("5. Sin extras")
                extras_opcion = input("Elija una opción: ")
                extras_seleccionados = []

                if extras_opcion == "1":
                    extras_seleccionados = ["Cebolla caramelizada"]
                elif extras_opcion == "2":  
                    extras_seleccionados = ["Queso extra"]
                elif extras_opcion == "3":
                    extras_seleccionados = ["Borde relleno de queso"]
                elif extras_opcion == "4":
                    extras_seleccionados = ["Aceitunas"]
                elif extras_opcion == "5":
                    extras_seleccionados = ["Sin extras"]
                else:
                    print("Opción no válida")
                director.build_personalizada(masa_seleccionada, salsa_seleccionada, ingredientes_seleccionados, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
                builder.product.list_parts()
                print("\n")



        else:
            print("Opción no válida")
        archivo_pedidos = 'pedidos.csv'
        archivo_existe = os.path.isfile(archivo_pedidos) and os.path.getsize(archivo_pedidos) > 0

        with open(archivo_pedidos, 'a', newline="") as file:
                            writer = csv.writer(file, delimiter=';')
                            if not archivo_existe:
                                writer.writerow(['Usuario','Tipo de Pizza', 'Masa', 'Cocción', 'Presentación', 'Maridaje', 'Extras', 'Ingredientes', 'Salsa'])
                            detalles = [usuario, pizza_seleccionada[0], masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado]
                            detalles.extend([', '.join(extras_seleccionados)])
                            if pizza_seleccionada == ["Personalizada"]:
                                detalles.append(', '.join(ingredientes_seleccionados))
                                detalles.append(salsa_seleccionada)
                            elif pizza_seleccionada == ["Barbacoa"]:
                                detalles.extend(['Ingredientes: carne, queso, bacon, cebolla, salsa barbacoa ', 'Salsa de barbacoa'])
                            elif pizza_seleccionada == ["Cuatro quesos"]:
                                detalles.extend(['Ingredientes: Mozzarella, Cheddar, Parmesano, Gorgonzola', 'Salsa de tomate'])
                            elif pizza_seleccionada == ["Jamón y Queso"]:
                                detalles.extend(['Ingredientes: Jamón, queso', 'Salsa de tomate'])
                            else:
                                print("Opción no válida")
                            writer.writerow(detalles)
        print('Has elegido', pizza_seleccionada)
        
    def leer_csv():
        archivo_pedidos = 'pedidos.csv'
        archivo_existe = os.path.isfile(archivo_pedidos) and os.path.getsize(archivo_pedidos) > 0
        if archivo_existe:
            with open(archivo_pedidos, 'r', newline="") as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    print('Su último pedido fue: ')
                    print('----------------------------')
                    #imprimir el pedido pero no el encabezado
                    if row[0] != 'Usuario':
                        print(f'Usuario: {row[0]}')
                        print(f'Tipo de pizza: {row[1]}')
                        print(f'Masa: {row[2]}')
                        print(f'Cocción: {row[3]}')
                        print(f'Presentación: {row[4]}')
                        print(f'Maridaje: {row[5]}')
                        print(f'Extras: {row[6]}')
                        if row[1] == "Personalizada":
                            print(f'Ingredientes: {row[7]}')
                            print(f'Salsa: {row[8]}')
                        else:
                            print(f'Ingredientes: {row[7]}')
                            print(f'Salsa: {row[8]}')
                        print('----------------------------')
        else:
            print("No hay pedidos registrados")
            
    leer_csv()

    def obtener_preferencias_usuario(usuario):
        archivo_pedidos = 'pedidos.csv'
        preferencias = {'masa': collections.defaultdict(int),
                        'coccion': collections.defaultdict(int),
                        'presentacion': collections.defaultdict(int),
                        'maridaje': collections.defaultdict(int)}
        # Asegúrate de que el archivo_pedidos existe y no está vacío antes de intentar abrirlo.
        try:
            with open(archivo_pedidos, 'r', newline="") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader, None)  # Saltar el encabezado
                for row in reader:
                    if row[0] == usuario:
                        preferencias['masa'][row[2]] += 1
                        preferencias['coccion'][row[3]] += 1
                        preferencias['presentacion'][row[4]] += 1
                        preferencias['maridaje'][row[5]] += 1
                        # Añadir lógica similar para ingredientes y extras si es necesario
        except FileNotFoundError:
            print(f"El archivo {archivo_pedidos} no existe.")
        except IndexError:
            print("El archivo CSV no tiene el formato esperado.")
        
        return preferencias
    obtener_preferencias_usuario('usuario')

    def recomendar_basado_en_historial(usuario, obtener_preferencias_usuario):
        preferencias = obtener_preferencias_usuario(usuario)
        
        # Encuentra las preferencias más comunes
        if preferencias['masa']:
            masa_recomendada = max(preferencias['masa'], key=preferencias['masa'].get)
        else:
            masa_recomendada = 'default_value' 

        if preferencias['coccion']:
            coccion_recomendada = max(preferencias['coccion'], key=preferencias['coccion'].get)
        else:
            coccion_recomendada = 'default_value'
        
        if preferencias['presentacion']:
            presentacion_recomendada = max(preferencias['presentacion'], key=preferencias['presentacion'].get)
        else:
            presentacion_recomendada = 'default_value'
        
        if preferencias['maridaje']:
            maridaje_recomendado = max(preferencias['maridaje'], key=preferencias['maridaje'].get)
        else:  
            maridaje_recomendado = 'default_value'

        print("Basado en tus pedidos anteriores, te recomendamos:")
        print(f"Masa: {masa_recomendada}")
        print(f"Cocción: {coccion_recomendada}")
        print(f"Presentación: {presentacion_recomendada}")
        print(f"Maridaje: {maridaje_recomendado}")
        # Imprimir recomendaciones de ingredientes y extras si se implementa

    # Llamar a la función de recomendaciones
    recomendar_basado_en_historial('nombre_del_usuario', obtener_preferencias_usuario)

Menu.Menu()

