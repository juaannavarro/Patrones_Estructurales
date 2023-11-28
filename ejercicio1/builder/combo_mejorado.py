from pizzas.infantil import ConstructorInfantil, infantil
from director import Director
from pizzas.jamonyqueso import Constructorjamonyqueso, jamonyqueso
from pizzas.barbacoa import ConstructorBarbacoa, Barbacoa
from pizzas.cuatroquesos import ConstructorcuatroQuesos, cuatroQuesos
from pizzas.personalizada import ConstructorPersonalizada, Personalizada
from composite import *
import csv
from datetime import datetime
class Combo:
    def __init__(self):
        self.combo_selected = []
        self.total_price = 0
        self.director = Director()

    def start(self):
        descuento = self.elegir_combo()
        precio_total_sin_descuento = self.total_price
        print(f'Precio total antes del descuento: {precio_total_sin_descuento:.2f}€')

        # Aplicar descuento
        self.total_price *= (1 - descuento)
        print(f"Descuento aplicado: {descuento * 100:.0f}%")
        print(f'Precio final después del descuento: {self.total_price:.2f}€')

        # Guardar en CSV
        self.guardar_pedido_en_csv(precio_total_sin_descuento, descuento)
    def elegir_combo(self):
        print("Elige un combo: ")
        print("1. Combo infantil")
        print("2. Combo familiar")
        print("3. Combo pareja")
        print('4. Sin combo')
        opcion = input("Opcion: ")

        if opcion == "1":
            self.combo_selected.append("Combo infantil")
            self.agregar_items_combo(1, 1, 1, 0)
            return 0.05 
        elif opcion == "2":
            self.combo_selected.append("Combo familiar")
            self.agregar_items_combo(4, 4, 4, 2)
            return 0.2
        elif opcion == "3":
            self.combo_selected.append("Combo pareja")
            self.agregar_items_combo(2, 2, 2, 1)
            return 0.1
        elif opcion == "4":
            self.combo_selected.append("Sin combo")
            print("Elija los items que desee: ")
            print("1. Pizzas")
            print("2. Bebidas")
            print("3. Postres")
            print("4. Entrantes")
            opcion = input("Opcion: ")
            
            if opcion == "1":
                print("Elija el número de pizzas que desee: ")
                num_pizzas = input("Opcion: ")
                self.agregar_items_combo(int(num_pizzas), 0, 0, 0)
            elif opcion == "2":
                print("Elija el número de bebidas que desee: ")
                num_bebidas = input("Opcion: ")
                self.agregar_items_combo(0, int(num_bebidas), 0, 0)
            elif opcion == "3":
                print("Elija el número de postres que desee: ")
                num_postres = input("Opcion: ")
                self.agregar_items_combo(0, 0, int(num_postres), 0)
            elif opcion == "4":
                print("Elija el número de entrantes que desee: ")
                num_entrantes = input("Opcion: ")
                self.agregar_items_combo(0, 0, 0, int(num_entrantes))
            return 0
        else:
            print("Opción no válida")
            return 0
        
    def agregar_items_combo(self, num_pizzas, num_bebidas, num_postres, num_entrantes):
        for _ in range(num_pizzas):
            self.elegir_pizzas()
        for _ in range(num_bebidas):
            self.elegir_item(bebidas, "bebida")
        for _ in range(num_postres):
            self.elegir_item(postres, "postre")
        for _ in range(num_entrantes):
            self.elegir_item(entrantes, "entrante")

    def elegir_entrante(self):
        self.elegir_item(entrantes, "entrante")
        pass

    def elegir_pizzas(self):
        print('1. Jamon y queso')
        print('2. Cuatro quesos')
        print('3. Barbacoa')
        print('4. Personalizada')
        
        opcion = input("Opcion: ")
        
        if opcion == "1":
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
            
            print("\nElija los extras (ingrese los números separados por comas):")
            print(extras.show())

            extras_opcion = input("Elija una opción o opciones: ")
            extras_seleccionados = []
            precio_extras = 0

            for opcion in extras_opcion.split(','):
                opcion = opcion.strip()  # Eliminar espacios en blanco
                if opcion.isdigit():
                    opcion = int(opcion) - 1
                    if 0 <= opcion < len(extras.children):
                        extra_seleccionado = extras.children[opcion]
                        extras_seleccionados.append(extra_seleccionado.name)
                        precio_extras += extra_seleccionado.get_price()

            # Construir la pizza con los extras seleccionados
            director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)

            descripcion_pizza = builder.product.list_parts()

            precio_pizza = builder.product.calculate_price() + precio_extras
            self.total_price += precio_pizza
            self.combo_selected.append(f"Pizza: {descripcion_pizza} - Precio: {precio_pizza}€")

        elif opcion == "2":
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
        

            
            print("\nElija los extras (ingrese los números separados por comas):")
            print(extras.show())

            extras_opcion = input("Elija una opción o opciones: ")
            extras_seleccionados = []
            precio_extras = 0

            for opcion in extras_opcion.split(','):
                opcion = opcion.strip()  # Eliminar espacios en blanco
                if opcion.isdigit():
                    opcion = int(opcion) - 1
                    if 0 <= opcion < len(extras.children):
                        extra_seleccionado = extras.children[opcion]
                        extras_seleccionados.append(extra_seleccionado.name)
                        precio_extras += extra_seleccionado.get_price()

            # Construir la pizza con los extras seleccionados
            director.build_cuatroQuesos(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)

            descripcion_pizza = builder.product.list_parts()

            precio_pizza = builder.product.calculate_price() + precio_extras
            self.total_price += precio_pizza
            self.combo_selected.append(f"Pizza: {descripcion_pizza} - Precio: {precio_pizza}€")
        elif opcion == "3":
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
        
            print("\nElija los extras (ingrese los números separados por comas):")
            print(extras.show())

            extras_opcion = input("Elija una opción o opciones: ")
            extras_seleccionados = []
            precio_extras = 0

            for opcion in extras_opcion.split(','):
                opcion = opcion.strip() 
                if opcion.isdigit():
                    opcion = int(opcion) - 1
                    if 0 <= opcion < len(extras.children):
                        extra_seleccionado = extras.children[opcion]
                        extras_seleccionados.append(extra_seleccionado.name)
                        precio_extras += extra_seleccionado.get_price()

            director.build_barbacoa(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)

            descripcion_pizza = builder.product.list_parts()

            precio_pizza = builder.product.calculate_price() + precio_extras
            self.total_price += precio_pizza
            self.combo_selected.append(f"Pizza: {descripcion_pizza} - Precio: {precio_pizza}€")
        elif opcion == "4":
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
                
                print("\nElija los extras (ingrese los números separados por comas):")
                print(extras.show())

                extras_opcion = input("Elija una opción o opciones: ")
                extras_seleccionados = []
                precio_extras = 0

                for opcion in extras_opcion.split(','):
                    opcion = opcion.strip()  # Eliminar espacios en blanco
                    if opcion.isdigit():
                        opcion = int(opcion) - 1
                        if 0 <= opcion < len(extras.children):
                            extra_seleccionado = extras.children[opcion]
                            extras_seleccionados.append(extra_seleccionado.name)
                            precio_extras += extra_seleccionado.get_price()

                # Construir la pizza con los extras seleccionados
                director.build_personalizada(masa_seleccionada, salsa_seleccionada, ingredientes_seleccionados, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
                descripcion_pizza = builder.product.list_parts()

                precio_pizza = builder.product.calculate_price() + precio_extras
                self.total_price += precio_pizza
                self.combo_selected.append(f"Pizza: {descripcion_pizza} - Precio: {precio_pizza}€")

                
        else:
            print("Opcion incorrecta")
        pass

        for item in self.combo_selected:
            print(item)
    def elegir_bebida(self):
        self.elegir_item(bebidas, "bebida")
        pass

    def elegir_postre(self):
        self.elegir_item(postres, "postre")
        pass
    
    def elegir_item(self, categoria, tipo):
        print(categoria.show())
        opcion = input(f"Seleccione un {tipo}: ")
        if opcion.isdigit():
            opcion = int(opcion) - 1
            if 0 <= opcion < len(categoria.children):
                item_seleccionado = categoria.children[opcion]
                self.combo_selected.append(f"{item_seleccionado.name} - {item_seleccionado.price}€")
                self.total_price += item_seleccionado.get_price()
            else:
                print("Opción no válida")
        else:
            print("Por favor, ingrese un número válido")
    def guardar_pedido_en_csv(self, precio_sin_descuento, descuento):
        # Asumiendo que self.combo_selected es una lista de strings que representan los ítems seleccionados
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos_pedido = {
            'fecha': fecha,
            'items': ', '.join(self.combo_selected),
            'precio_sin_descuento': precio_sin_descuento,
            'descuento': f"{descuento * 100}%",
            'precio_final': self.total_price
        }

        with open('pedidos.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=datos_pedido.keys())
            
            # Escribir la cabecera solo si el archivo está vacío (posiblemente sea la primera escritura)
            archivo_csv.seek(0, 2)  # Moverse al final del archivo
            if archivo_csv.tell() == 0:  # Verificar si el archivo está vacío
                escritor_csv.writeheader()  # Escribir la cabecera

            escritor_csv.writerow(datos_pedido)

combo = Combo()
combo.start()
