


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

extras = MenuCategory("Extras")
extras.add(MenuItem("1.Queso extra", 1.0))
extras.add(MenuItem("2.Borde relleno de queso", 2.0))
extras.add(MenuItem("3.Aceitunas", 1.0))
extras.add(MenuItem("4.Cebolla caramelizada", 1.0))
extras.add(MenuItem("5.Maíz", 1.0))
extras.add(MenuItem("6.Sin extras", 0.0))