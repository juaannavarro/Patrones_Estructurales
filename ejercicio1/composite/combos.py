from builder.pizzas.infantil import *
from builder.director import *
class Combo:
    print("Elige un combo: ")
    print("1. Combo infantil")
    print("2. Combo familiar")
    print("3. Combo pareja")
    
    opcion = input("Opcion: ")
    combo_selected = []
    if opcion == "1":
        combo_selected=["Combo infantil"]
        director = Director()
        builder = ConstructorInfantil()
        director.builder = builder
        
        director.build_infantil("Masa fina", "Horno", "Cuadrada", "Coca cola", ["Patatas fritas", "Helado"])
        combo_selected.append(builder.product.list_parts())
        print("Combo infantil creado: ")
        print(builder.product.list_parts())
    elif opcion == "2":
        combo_selected=["Combo familiar"]
        director = Director()
        builder = ConstructorInfantil()
        director.builder = builder
        
        director.build_infantil("Masa fina", "Horno", "Cuadrada", "Coca cola", ["Patatas fritas", "Helado"])
        combo_selected.append(builder.product.list_parts())
        print("Combo familiar creado: ")
        print(builder.product.list_parts())
        
    elif opcion == "3":
        combo_selected=["Combo pareja"]
        director = Director()
        builder = ConstructorInfantil()
        director.builder = builder
        
        director.build_infantil("Masa fina", "Horno", "Cuadrada", "Coca cola", ["Patatas fritas", "Helado"])
        combo_selected.append(builder.product.list_parts())
        print("Combo pareja creado: ")
        print(builder.product.list_parts())
        
    else:
        
        print("Opcion incorrecta")  
        
    print("Combo seleccionado: ")
    print(combo_selected)
    
    print("Gracias por su compra")
    
    print("Vuelva pronto")
    
Combo()
        
        
        
        

    