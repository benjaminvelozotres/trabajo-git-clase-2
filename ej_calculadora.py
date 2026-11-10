# ============================================================
# Ejercicio Simón - Calculadora básica
# ------------------------------------------------------------
# Objetivo: hacer operaciones matemáticas con dos números
# ingresados por el usuario.
# Conceptos: conversión de tipos (float), operadores
# aritméticos (+ - * /) y control de errores con if.
# ============================================================

# input() siempre devuelve texto, por eso usamos float()
# para convertirlo en un número con decimales.
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

print("Suma:          ", a + b)
print("Resta:         ", a - b)
print("Multiplicación:", a * b)

# No se puede dividir por cero: lo verificamos antes con un if.
if b != 0:
    print("División:      ", a / b)
else:
    print("División:       no se puede dividir por cero")