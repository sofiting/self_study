"""
declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y 
nos mostrará el precio final de la fruta a partir de los datos guardados 
en el diccionario. Si la fruta no existe nos dará un error. 
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

precios={"manzana":2,"naranja":1.5,"platano":4,"piña":3}
sal = True
while sal:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower( )not in precios:
        print("Fruta no existe")
    else:
        cantidad = int(input("Dime la cantidad de frutas que has vandido:"))
        print("El precio es de %s"%(cantidad*precios[fruta.lower()]))
        
        while True:
            opcion=input("Quieres vender otra fruta ? (s/n)")
            if opcion.lower()=="n" or opcion.lower()=="s":
                if opcion.lower()=="n":
                    sal=False
                break