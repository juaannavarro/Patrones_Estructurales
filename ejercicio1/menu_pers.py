

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}€"


class MenuPersonalizado:
    def __init__(self):
        self.entrantes = []
        self.bebidas = []
        self.pizzas = []  # Aquí asumimos que las pizzas se crean con un sistema diferente
        self.postres = []

    def add_entrante(self, entrante):
        self.entrantes.append(entrante)

    def add_bebida(self, bebida):
        self.bebidas.append(bebida)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def add_postre(self, postre):
        self.postres.append(postre)

    def mostrar_menu(self):
        print("Menú")
        print("-----")
        print("Entrantes:")
        for item in self.entrantes:
            print(item)
        print("\nBebidas:")
        for item in self.bebidas:
            print(item)
        print("\nPizzas:")
        for item in self.pizzas:
            print(item)
        print("\nPostres:")
        for item in self.postres:
            print(item)

# Crear el menú
menu = MenuPersonalizado()

# Añadir ítems al menú
menu.add_entrante(MenuItem("Pan de Ajo", 3.50))
menu.add_bebida(MenuItem("Coca-Cola", 2.00))
menu.add_pizza(MenuItem("Pizza Margarita", 8.00))  # Asumimos que esta es una instancia de tu clase Pizza
menu.add_postre(MenuItem("Gelato", 4.00))

# Mostrar el menú
menu.mostrar_menu()
