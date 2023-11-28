from pizzas.infantil import ConstructorInfantil, infantil
from director import Director
from pizzas.jamonyqueso import Constructorjamonyqueso, jamonyqueso
from pizzas.barbacoa import ConstructorBarbacoa, Barbacoa
from pizzas.cuatroquesos import ConstructorcuatroQuesos, cuatroQuesos
from pizzas.personalizada import ConstructorPersonalizada, Personalizada
class MenuComponent:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} - {self.price}€"

    def get_price(self):
        return self.price

class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}€"
    def get_price(self):
        return self.price
class MenuCategory(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show(self):
        result = f"{self.name}:\n"
        for child in self.children:
            result += f"  - {child.show()}\n"
        return result
    
entrantes = MenuCategory("Entrantes")
entrantes.add(MenuItem("Patatas fritas", 2.5))
entrantes.add(MenuItem("Nuggets", 3.0))
# ... Añadir más entrantes

bebidas = MenuCategory("Bebidas")
bebidas.add(MenuItem("Coca-cola", 1.5))
bebidas.add(MenuItem("Fanta", 1.5))
# ... Añadir más bebidas

postres = MenuCategory("Postres")
postres.add(MenuItem("Helado", 2.0))
postres.add(MenuItem("Tarta de chocolate", 2.5))


class Combo:
    def __init__(self):
        self.combo_selected = []
        self.director = Director()
        self.total_price = 0
        self.elegir_combo()
        self.elegir_entrante()
        self.elegir_pizzas()
        self.elegir_bebida()
        self.elegir_postre()
        print(self.combo_selected)
        print(f'El precio total es: {self.total_price}€')

    def elegir_combo(self):
        print("Elige un combo: ")
        print("1. Combo infantil")
        print("2. Combo familiar")
        print("3. Combo pareja")
        opcion = input("Opcion: ")
        if opcion == "1":
            self.combo_selected.append("Combo infantil")


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
            descripcion_pizza = builder.product.list_parts()
            pizza_seleccionada.append(descripcion_pizza)
            self.combo_selected.append("Pizza: " + ", ".join(pizza_seleccionada))

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
            
            director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)    
            descripcion_pizza = builder.product.list_parts()
            pizza_seleccionada.append(descripcion_pizza)
            self.combo_selected.append("Pizza: " + ", ".join(pizza_seleccionada))
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
            
            director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)    
            descripcion_pizza = builder.product.list_parts()
            pizza_seleccionada.append(descripcion_pizza)
            self.combo_selected.append("Pizza: " + ", ".join(pizza_seleccionada))
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
                director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)    
                descripcion_pizza = builder.product.list_parts()
                pizza_seleccionada.append(descripcion_pizza)
                self.combo_selected.append("Pizza: " + ", ".join(pizza_seleccionada))

                
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

# Ejecutar el proceso
Combo()
