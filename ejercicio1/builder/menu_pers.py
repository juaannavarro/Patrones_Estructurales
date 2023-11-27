from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def show(self) -> str:
        pass

class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self) -> str:
        return f"{self.name} - {self.price}€"


class MenuCategory(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: MenuComponent):
        self.children.append(component)

    def remove(self, component: MenuComponent):
        self.children.remove(component)

    def show(self) -> str:
        result = f"{self.name}:\n"
        for child in self.children:
            result += f"  {child.show()}\n"
        return result

# Creando elementos del menú
entrante = MenuItem("Pan de Ajo", 3.50)
bebida = MenuItem("Coca-Cola", 2.00)
# Suponiendo que tienes una clase Pizza
pizza = MenuItem("Pizza Margarita", 8.50) # Reemplazar con la instancia de tu clase de pizza
postre = MenuItem("Gelato", 4.00)

# Creando categorías del menú
menu_entrantes = MenuCategory("Entrantes")
menu_bebidas = MenuCategory("Bebidas")
menu_pizzas = MenuCategory("Pizzas")
menu_postres = MenuCategory("Postres")

# Añadiendo ítems a las categorías
menu_entrantes.add(entrante)
menu_bebidas.add(bebida)
menu_pizzas.add(pizza) # Aquí añadirías la instancia de tu pizza
menu_postres.add(postre)

# Creando menú principal
menu_principal = MenuCategory("Menú Principal")
menu_principal.add(menu_entrantes)
menu_principal.add(menu_bebidas)
menu_principal.add(menu_pizzas)
menu_principal.add(menu_postres)

# Mostrando el menú
print(menu_principal.show())
