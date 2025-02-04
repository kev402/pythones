from pythones import *

imprimir("Hola, mundo")

valor = ingresar("Escribe algo: ")
imprimir(f"Escribiste: {valor}")

lista_numeros = [1, 2, 3, 4, 5]
total = sumar(lista_numeros)
imprimir(f"La suma de la lista es: {total}")

comando("dir", Verdadero, Verdadero)

def accion_simple():
    imprimir("Acción ejecutada")

ejecutar_accion(accion_simple)

si(Verdadero, accion_simple)
si_contrario(Falso, accion_simple)

detener_bucle = Falso

def condicion_bucle():
    return True

def accion_bucle():
    imprimir("Acción en bucle")
    return Falso

mientras(condicion_bucle, accion_bucle)

detener()

resultado_accion = retorno(lambda: "Resultado de la acción")
imprimir(resultado_accion)

imprimir(no(Falso))

imprimir(ó(Verdadero, Falso))

imprimir(y(Verdadero, Verdadero))

def intento_exitoso():
    return "Éxito"

def intento_erroneo():
    raise ValueError("Error intencional")

imprimir(intentar(intento_exitoso, (ValueError,), "Error manejado"))
imprimir(intentar(intento_erroneo, (ValueError,), "Error manejado"))

matematicas = importar("math")
imprimir(matematicas.sqrt(16))

def imprimir_elemento(elemento):
    imprimir(f"Elemento: {elemento}")

para(lista_numeros, imprimir_elemento)