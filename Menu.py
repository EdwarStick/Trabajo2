#Operaciones de la calculadora#
def main():
while True:
print("Calculadora")
print("1. Suma")
print("2. Resta")
print("3. Salir")

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
print("Saliendo...")
break
case _:
print("Opción no válida")

if __name__ == "__main__":
main()