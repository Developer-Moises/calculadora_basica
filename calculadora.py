# calculadora.py
# Script básico para operaciones matemáticas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")
if operacion == '+':
    print(f"Resultado de la suma de {numero_1} + {numero_2}:", numero_1 + numero_2)
elif operacion == '-':
    print(f"Resultado de la resta de {numero_1} - {numero_2}:", numero_1 - numero_2)
elif operacion == '*':
    print(f"Resultado de la multiplicación de {numero_1} * {numero_2}:", numero_1 * numero_2)
elif operacion == '/':
    if numero_2 != 0:
        print(f"Resultado de la división de {numero_1} / {numero_2}:", numero_1 / numero_2)
    else:
        print("Error: no se puede dividir por cero.")
else:
 print("Operación no válida.")