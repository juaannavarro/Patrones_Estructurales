from combo_mejorado import *

if __name__ == '__main__':

    combo = Combo()
    combo.start()
    pedidos = combo.cargar_pedidos_desde_csv()
    for pedido in pedidos:
        print(pedido)

    reconstructor = MenuReconstructor('pedidos.csv')
    pedidos_reconstruidos = reconstructor.reconstruir_menu()
    for pedido in pedidos_reconstruidos:
        print(pedido)