from pizzeria import Pizzeria
from director import Director
from menu import Menu

if __name__ == '__main__':

    director = Director()
    constructor = Pizzeria()
    director.builder = constructor
    menu = Menu()
