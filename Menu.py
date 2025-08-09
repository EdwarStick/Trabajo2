from funciones import suma, resta, multiplicacion, division

def main():
    while True:
        print("Calculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        match opcion: 
            case "1":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {suma(a, b)}")  
            case "2":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {resta(a, b)}") 
            case "3":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {multiplicacion(a, b)}")
            case "4":
                a = float(input("Primer número: "))
                b = float(input("Segundo número: "))
                print(f"Resultado: {division(a, b)}")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")

if _name_ == "_main_":
    main()