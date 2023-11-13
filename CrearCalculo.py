numero1 = float(input("Elige tu primer numero: "))
numero2 = float(input("Elige tu segundo numero: "))

opcion = 0
while True:
    print("""
        Elige una opcion:
        
        1) Sumar
        2) Restar
        3) Multiplicar
        4) Division
        5) Salir
        """)
    
    opcion = int(input("Elige una opcion: "))
    
    if opcion == 1:
        print("")
        print("La suma de ", numero1,"+",numero2,"el resultado es",numero1+numero2)
    elif opcion == 2:
        print("")
        print("La resta de ", numero1,"-",numero2,"el resultado es",numero1-numero2)
    elif opcion == 3:
        print("")
        print("La multiplicacion de ", numero1,"*",numero2,"el resultado es",numero1*numero2)
    elif opcion == 4:
        print("")
        print("La division de ", numero1,"/",numero2,"el resultado es",numero1//numero2)
    elif opcion == 5:
        break
    else:
        print("Opcion Incorrecta")
        
        