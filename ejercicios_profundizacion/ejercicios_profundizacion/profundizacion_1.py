# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
primer_num= int (input("Ingrese un número: "))
segundo_num= int (int (input("Ingrese  otro número: ")))

suma = primer_num + segundo_num
print(f"La suma entre {primer_num} y {segundo_num} es: {suma} ")
resta= primer_num - segundo_num
print(f"La resta entre {primer_num} y {segundo_num} es: {resta}")
multiplicacion = primer_num * segundo_num
print(f"La multiplicación entre {primer_num} y {segundo_num} es: {multiplicacion}")
division= primer_num /segundo_num
print(f"La división entre {primer_num} y {segundo_num} es: {division}")
exponente = primer_num**segundo_num 
print(f"El exponente de {primer_num} elevado a {segundo_num} es: {exponente}")



