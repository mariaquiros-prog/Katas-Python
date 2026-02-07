"""
PROYECTO LÓGICA: Katas de Python
Alumno: María Quirós
"""

from functools import reduce
import math

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados. [cite: 2, 3]
def contar_frecuencias(texto: str) -> dict:
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

# --- PRUEBA DEL EJERCICIO 1 ---
print(f"Ej 1: {contar_frecuencias('hola mundo')}")

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map() [cite: 4]
def duplicar_valores(numeros: list) -> list:
    return list(map(lambda x: x * 2, numeros))

# --- PRUEBA DEL EJERCICIO 2 ---
print(f"Ej 2: {duplicar_valores([1, 2, 3])}")

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras que contengan la palabra objetivo. [cite: 5, 6]
def filtrar_por_objetivo(lista_palabras: list, objetivo: str) -> list:
    return [p for p in lista_palabras if objetivo in p]

# --- PRUEBA DEL EJERCICIO 3 ---
print(f"Ej 3: {filtrar_por_objetivo(['python', 'progra'], 'progra')}")

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map() [cite: 7]
def calcular_diferencia_listas(lista1: list, lista2: list) -> list:
    return list(map(lambda a, b: a - b, lista1, lista2))

# --- PRUEBA DEL EJERCICIO 4 ---
print(f"Ej 4: {calcular_diferencia_listas([10, 20], [1, 2])}")

# 5. Escribe una función que tome una lista de números y un valor opcional nota_aprobado (defecto 5). Debe devolver una tupla con la media y el estado ("aprobado"/"suspenso"). [cite: 8, 9, 10]
def verificar_estado_academico(notas: list, nota_aprobado: float = 5) -> tuple:
    media = sum(notas) / len(notas) if notas else 0
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# --- PRUEBA DEL EJERCICIO 5 ---
print(f"Ej 5: {verificar_estado_academico([4, 6, 8])}")

# 6. Escribe una función que calcule el factorial de un número de manera recursiva. [cite: 11]
def factorial_recursivo(n: int) -> int:
    if n <= 1: return 1
    return n * factorial_recursivo(n - 1)

# --- PRUEBA DEL EJERCICIO 6 ---
print(f"Ej 6: Factorial de 5 es {factorial_recursivo(5)}")

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map() [cite: 12]
def convertir_tuplas_a_strings(lista_tuplas: list) -> list:
    return list(map(str, lista_tuplas))

# --- PRUEBA DEL EJERCICIO 7 ---
print(f"Ej 7: {convertir_tuplas_a_strings([(1,2), (3,4)])}")

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Maneja excepciones de valor no numérico o división por cero. [cite: 13, 14, 15]
def division_segura():
    try:
        n1 = float(input("Ej 8 - Dividendo: "))
        n2 = float(input("Ej 8 - Divisor: "))
        print(f"Resultado exitoso: {n1 / n2}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Operación no exitosa: {e}")

# --- PRUEBA DEL EJERCICIO 8 ---
division_segura()

# 9. Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva excluyendo ciertas mascotas prohibidas en España. Usa filter(). [cite: 16, 17]
def filtrar_mascotas_permitidas(lista: list) -> list:
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista))

# --- PRUEBA DEL EJERCICIO 9 ---
print(f"Ej 9: {filtrar_mascotas_permitidas(['Perro', 'Tigre'])}")

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si está vacía, lanza una excepción personalizada. [cite: 18, 19]
class ListaVaciaError(Exception): pass

def promedio_con_error(numeros: list) -> float:
    if not numeros: raise ListaVaciaError("Error: Lista vacía.")
    return sum(numeros) / len(numeros)

# --- PRUEBA DEL EJERCICIO 10 ---
try: print(f"Ej 10: {promedio_con_error([10, 20])}")
except ListaVaciaError as e: print(e)

# 11. Programa que pida al usuario su edad y maneje valores no numéricos o fuera de rango (0-120). [cite: 20, 21]
def validar_edad():
    try:
        edad = int(input("Ej 11 - Introduce edad: "))
        if 0 <= edad <= 120: print(f"Edad validada: {edad}")
        else: print("Edad fuera de rango.")
    except ValueError: print("Valor no numérico.")

# --- PRUEBA DEL EJERCICIO 11 ---
validar_edad()

# 12. Función que devuelva una lista con la longitud de cada palabra de una frase. Usa map() [cite: 22, 23]
def longitud_palabras(frase: str) -> list:
    return list(map(len, frase.split()))

# --- PRUEBA DEL EJERCICIO 12 ---
print(f"Ej 12: {longitud_palabras('Hola Mundo')}")

# 13. Genera una función que para un conjunto de caracteres devuelva una lista de tuplas (MAYUS, minus) sin repetir. [cite: 24, 25]
def transformar_letras(caracteres: list) -> list:
    return [(c.upper(), c.lower()) for c in set(caracteres)]

# --- PRUEBA DEL EJERCICIO 13 ---
print(f"Ej 13: {transformar_letras(['a', 'b', 'a'])}")

# 14. Función que retorne palabras que comiencen con una letra específica. Usa filter() [cite: 26, 27]
def filtrar_por_letra(lista: list, letra: str) -> list:
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

# --- PRUEBA DEL EJERCICIO 14 ---
print(f"Ej 14: {filtrar_por_letra(['Casa', 'Coche', 'Bici'], 'C')}")

# 15. Crea una función Lambda que sume 3 a cada número de una lista. [cite: 28]
sumar_3 = lambda lista: [n + 3 for n in lista]

# --- PRUEBA DEL EJERCICIO 15 ---
print(f"Ej 15: {sumar_3([1, 2, 3])}")

# 16. Función que devuelva palabras más largas que n. Usa filter() [cite: 29, 30]
def filtrar_por_n(texto: str, n: int) -> list:
    return list(filter(lambda p: len(p) > n, texto.split()))

# --- PRUEBA DEL EJERCICIO 16 ---
print(f"Ej 16: {filtrar_por_n('Python es genial', 3)}")

# 17. Lista de dígitos a número correspondiente. Usa reduce() [cite: 31, 32]
def lista_a_numero(digitos: list) -> int:
    return reduce(lambda x, y: x * 10 + y, digitos)

# --- PRUEBA DEL EJERCICIO 17 ---
print(f"Ej 17: {lista_a_numero([5, 7, 2])}")

# 18. Filtra estudiantes con calificación >= 90 de una lista de diccionarios. Usa filter() [cite: 33]
def estudiantes_top(estudiantes: list) -> list:
    return list(filter(lambda e: e['calificacion'] >= 90, estudiantes))

# --- PRUEBA DEL EJERCICIO 18 ---
print(f"Ej 18: {estudiantes_top([{'nombre': 'A', 'calificacion': 95}, {'nombre': 'B', 'calificacion': 80}])}")

# 19. Crea una función Lambda que filtre números impares. [cite: 34]
filtrar_impares = lambda lista: list(filter(lambda n: n % 2 != 0, lista))

# --- PRUEBA DEL EJERCICIO 19 ---
print(f"Ej 19: {filtrar_impares([1, 2, 3, 4])}")

# 20. De una lista mixta obtén solo valores int. Usa filter() [cite: 35, 36]
def solo_enteros(lista: list) -> list:
    return list(filter(lambda x: isinstance(x, int), lista))

# --- PRUEBA DEL EJERCICIO 20 ---
print(f"Ej 20: {solo_enteros([1, 'a', 2, True])}")

# 21. Calcula el cubo de un número mediante Lambda. [cite: 37]
cubo = lambda x: x ** 3

# --- PRUEBA DEL EJERCICIO 21 ---
print(f"Ej 21: El cubo de 3 es {cubo(3)}")

# 22. Producto total de una lista numérica. Usa reduce(). [cite: 38]
def producto_total(lista: list) -> int:
    return reduce(lambda x, y: x * y, lista)

# --- PRUEBA DEL EJERCICIO 22 ---
print(f"Ej 22: {producto_total([2, 3, 4])}")

# 23. Concatena una lista de palabras. Usa reduce(). [cite: 39]
def unir_palabras(lista: list) -> str:
    return reduce(lambda x, y: x + y, lista)

# --- PRUEBA DEL EJERCICIO 23 ---
print(f"Ej 23: {unir_palabras(['Hola', 'Mundo'])}")

# 24. Calcula la diferencia total en una lista. Usa reduce(). [cite: 40]
def resta_total(lista: list) -> int:
    return reduce(lambda x, y: x - y, lista)

# --- PRUEBA DEL EJERCICIO 24 ---
print(f"Ej 24: {resta_total([100, 20, 10])}")

# 25. Función que cuente caracteres en una cadena. [cite: 41]
def largo_cadena(cadena: str) -> int:
    return len(cadena)

# --- PRUEBA DEL EJERCICIO 25 ---
print(f"Ej 25: {largo_cadena('Python')}")

# 26. Lambda que calcule el resto de una división. [cite: 43]
resto = lambda a, b: a % b

# --- PRUEBA DEL EJERCICIO 26 ---
print(f"Ej 26: Resto de 10/3 es {resto(10, 3)}")

# 27. Función que calcule el promedio de una lista. [cite: 44]
def promedio_simple(lista: list) -> float:
    return sum(lista) / len(lista) if lista else 0

# --- PRUEBA DEL EJERCICIO 27 ---
print(f"Ej 27: {promedio_simple([10, 20, 30])}")

# 28. Devuelve el primer elemento duplicado. [cite: 45]
def primer_duplicado(lista: list):
    vistos = set()
    for x in lista:
        if x in vistos: return x
        vistos.add(x)
    return None

# --- PRUEBA DEL EJERCICIO 28 ---
print(f"Ej 28: {primer_duplicado([1, 2, 3, 2, 1])}")

# 29. Enmascara con '#' excepto los últimos cuatro caracteres. [cite: 46]
def enmascarar(valor) -> str:
    v = str(valor)
    return "#" * (len(v) - 4) + v[-4:] if len(v) > 4 else v

# --- PRUEBA DEL EJERCICIO 29 ---
print(f"Ej 29: {enmascarar('12345678')}")

# 30. Determine si dos palabras son anagramas. [cite: 47]
def es_anagrama(p1: str, p2: str) -> bool:
    return sorted(p1.lower()) == sorted(p2.lower())

# --- PRUEBA DEL EJERCICIO 30 ---
print(f"Ej 30: ¿Amor y Roma? {es_anagrama('Amor', 'Roma')}")

# 31. Solicita nombres y busca uno; si no está, lanza excepción. [cite: 48, 49]
def buscar_usuario():
    nombres = ["Ana", "Juan"]
    b = input("Ej 31 - Buscar nombre (Ana/Juan): ")
    if b not in nombres: raise Exception("No encontrado")
    print("Encontrado")

# --- PRUEBA DEL EJERCICIO 31 ---
try: buscar_usuario()
except Exception as e: print(e)

# 32. Busca nombre en lista de empleados y devuelve puesto o error. [cite: 50]
def buscar_empleado(nombre: str, lista: list):
    for e in lista:
        if e['nombre'] == nombre: return e['puesto']
    return "La persona no trabaja aquí."

# --- PRUEBA DEL EJERCICIO 32 ---
print(f"Ej 32: {buscar_empleado('Ana', [{'nombre': 'Ana', 'puesto': 'Dev'}])}")

# 33. Lambda que sume elementos correspondientes de dos listas. [cite: 51]
sumar_listas = lambda l1, l2: [a + b for a, b in zip(l1, l2)]

# --- PRUEBA DEL EJERCICIO 33 ---
print(f"Ej 33: {sumar_listas([1, 2], [3, 4])}")

# 34-35. Clase Arbol: tronco, ramas y métodos de crecimiento. [cite: 52, 53, 56, 57, 58, 59, 60, 62]
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self): self.tronco += 1
    def nueva_rama(self): self.ramas.append(1)
    def crecer_ramas(self): self.ramas = [r + 1 for r in self.ramas]
    def quitar_rama(self, pos: int):
        if 0 <= pos < len(self.ramas): self.ramas.pop(pos)
    def info_arbol(self):
        return f"Tronco: {self.tronco}, Ramas: {len(self.ramas)}, Long: {self.ramas}"

# --- PRUEBA DEL EJERCICIO 34-35 ---
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
print(f"Ej 34-35: {mi_arbol.info_arbol()}")

# 36. Clase UsuarioBanco: nombre, saldo, cuenta corriente y operaciones. [cite: 71, 72, 74, 75, 77, 79]
class UsuarioBanco:
    def __init__(self, nombre, saldo, cc):
        self.nombre = nombre
        self.saldo = saldo
        self.cc = cc
    def agregar(self, c): self.saldo += c
    def retirar(self, c):
        if c > self.saldo: raise Exception("Saldo insuficiente")
        self.saldo -= c
    def transferir(self, otro, c):
        self.retirar(c)
        otro.agregar(c)

# --- PRUEBA DEL EJERCICIO 36 ---
u1 = UsuarioBanco("Alicia", 100, True)
u2 = UsuarioBanco("Bob", 50, True)
u2.agregar(20)
u2.transferir(u1, 10)
print(f"Ej 36: {u1.nombre} tiene {u1.saldo}, {u2.nombre} tiene {u2.saldo}")

# 37. Función procesar_texto con opciones: contar, reemplazar, eliminar. [cite: 87, 96]
def procesar_texto(texto: str, opcion: str, *args):
    if opcion == "contar": return {p: texto.split().count(p) for p in set(texto.split())}
    if opcion == "reemplazar": return texto.replace(args[0], args[1])
    if opcion == "eliminar": return texto.replace(args[0], "")

# --- PRUEBA DEL EJERCICIO 37 ---
print(f"Ej 37: {procesar_texto('hola hola mundo', 'contar')}")

# 38. Programa que diga si es de noche, día o tarde según la hora. [cite: 99]
def momento_dia(h):
    if 6 <= h <= 13: return "Día"
    elif 14 <= h <= 20: return "Tarde"
    else: return "Noche"

# --- PRUEBA DEL EJERCICIO 38 ---
print(f"Ej 38: A las 15 es {momento_dia(15)}")

# 39. Clasificación de calificación numérica a texto. [cite: 100, 101, 102, 103, 104, 105]
def calificacion_texto(n):
    if n <= 69: return "insuficiente"
    elif n <= 79: return "bien"
    elif n <= 89: return "muy bien"
    else: return "excelente"

# --- PRUEBA DEL EJERCICIO 39 ---
print(f"Ej 39: Un 85 es {calificacion_texto(85)}")

# 40. Calcula área según Figura y datos. [cite: 106]
def calcular_area(fig, datos):
    if fig == "rectangulo": return datos[0] * datos[1]
    elif fig == "circulo": return math.pi * (datos[0]**2)
    elif fig == "triangulo": return (datos[0] * datos[1]) / 2

# --- PRUEBA DEL EJERCICIO 40 ---
print(f"Ej 40: Area triángulo (10,5): {calcular_area('triangulo', (10, 5))}")

# 41. Determinar monto final de compra con cupón de descuento. [cite: 107, 108, 109, 110, 111, 112, 114, 115]
def caja_final():
    precio = float(input("Ej 41 - Precio original: "))
    if input("¿Cupón? (si/no): ") == "si":
        desc = float(input("Valor descuento: "))
        if desc > 0: precio -= desc
    print(f"Precio final: {max(0, precio)}")

# --- PRUEBA DEL EJERCICIO 41 ---
caja_final()