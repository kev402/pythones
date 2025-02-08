from pythones import *

# 1. Demostración básica de impresión e ingreso de datos.
imprimir("Hola, mundo")
valor = ingresar("Escribe algo: ")
imprimir(f"Escribiste: {valor}")

# 2. Uso de la función sumar.
lista_numeros = [1, 2, 3, 4, 5]
total = sumar(lista_numeros)
imprimir(f"La suma de la lista es: {total}")

# 3. Uso de la función comando para ejecutar un comando en el sistema.
#    (Ten en cuenta que "dir" funciona en Windows; en otros sistemas puede usarse "ls".)
comando("dir", Verdadero, Verdadero)

# 4. Definición y ejecución de una acción simple.
def accion_simple():
    imprimir("Acción ejecutada")

ejecutar_accion(accion_simple)

# 5. Uso de condicionales: si y si_contrario.
si(Verdadero, accion_simple)
si_contrario(Falso, accion_simple)

# 6. Uso de la función mientras. No es necesario definir 'detener_bucle' externamente,
#    ya que el módulo lo maneja internamente.
def condicion_bucle():
    return True

def accion_bucle():
    imprimir("Acción en bucle")
    # Al devolver Falso se rompe el bucle (ya que en 'mientras' se evalúa "if not ejecutar_accion(accion)")
    return Falso

mientras(condicion_bucle, accion_bucle)

# 7. Uso de detener() para finalizar un bucle (aunque en este ejemplo el bucle ya terminó).
detener()

# 8. Uso de retorno: se retorna una función; para obtener su resultado es necesario llamarla.
resultado_accion = retorno(lambda: "Resultado de la acción")
imprimir(resultado_accion())  # Se llama a la función retornada

# 9. Uso de las funciones no, ó (or) y y (and).
imprimir(no(Falso))
imprimir(ó(Verdadero, Falso))
imprimir(y(Verdadero, Verdadero))

# 10. Uso de intentar para manejar excepciones.
def intento_exitoso():
    return "Éxito"

def intento_erroneo():
    raise ValueError("Error intencional")

imprimir(intentar(intento_exitoso, (ValueError,), "Error manejado"))
imprimir(intentar(intento_erroneo, (ValueError,), "Error manejado"))

# 11. Uso de importar para cargar dinámicamente un módulo.
matematicas = importar("math")
imprimir(matematicas.sqrt(16))

# 12. Uso de para para iterar sobre un iterable.
def imprimir_elemento(elemento):
    imprimir(f"Elemento: {elemento}")

para(lista_numeros, imprimir_elemento)

# --- Funciones adicionales del módulo que faltaban en el código original ---

# 13. Demostración de la función contrario.
contrario(lambda: imprimir("Ejecutando función contrario"))

# 14. Demostración de las funciones es y no_es para comparar identidades de objetos.
a = [1, 2, 3]
b = a  # Mismo objeto
c = [1, 2, 3]  # Objeto distinto, aunque con el mismo contenido
imprimir(f"es(a, b): {es(a, b)}")       # Debería ser True.
imprimir(f"no_es(a, c): {no_es(a, c)}")   # Debería ser True.

# 15. Demostración de funciones de conversión y redondeo.
imprimir(f"ent('100'): {ent('100')}")
imprimir(f"decim('3.14'): {decim('3.14')}")
imprimir(f"cad(123): {cad(123)}")
imprimir(f"redondear(3.14159, 3): {redondear(3.14159, 3)}")
