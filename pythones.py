"""pythones - Un módulo que permite escribir código de python en español y con una sintaxis basada en funciones.
Creado por kev402 - repositorio: https://github.com/kev402 y https://github.com/kev402/pythones
Las librerías usadas para este proyecto son estandares de python.
Una vez obtenga este archivo lo puede instalar usando el comando python setup.py install en windows y en sistemas unix python3 setup.py install.
Para importarlo en su código use from pythones import *
Para más información visite el repositorio de github."""

import subprocess
import importlib

Verdadero = True
Falso = False

def imprimir(entrada):
    """Imprime contenido en la consola, de la misma forma que print."""
    print(entrada)

def ingresar(contenido):
    """Solicita que se ingrese contenido y se puede poner anunciamientos para hacer la solicitud."""
    return input(contenido)

def sumar(iterable, inicial=0):
    """Suma los elementos de un iterable y devuelve el resultado."""
    total = inicial
    for elemento in iterable:
        total += elemento
    return total

def comando(entrada, bool1: bool, bool2: bool):
    """Usa subprocess para correr comandos en la consola, usando shell y check, que pueden ser ajustados con valores booleanos."""
    return subprocess.run(entrada, shell=bool1, check=bool2)

def ejecutar_accion(accion):
    if callable(accion):
        return accion()
    elif isinstance(accion, (list, tuple)):
        for act in accion:
            if callable(act):
                act()
    else:
        raise ValueError("La acción debe ser una función o una lista de funciones.")

def si(condicion, accion):
    """Ejecuta una acción si la condición es verdadera, de forma parecida a if."""
    if condicion:
        ejecutar_accion(accion)

def si_contrario(condicion, accion):
    """Ejecuta una acción si la condición es falsa, de forma parecida a elif."""
    if not condicion:
        ejecutar_accion(accion)

def contrario(accion):
    """Ejecuta una acción si todas las condiciones son falsas, de forma parecida a else."""
    ejecutar_accion(accion)

def mientras(condicion, accion):
    """Ejecuta una acción mientras la condición sea verdadera, de forma parecida a while."""
    global detener_bucle
    detener_bucle = False
    while condicion() and not detener_bucle:
        if not ejecutar_accion(accion):
            break

def detener():
    """Detiene el bucle mientras."""
    global detener_bucle
    detener_bucle = True

def retorno(accion):
    """Retorna una acción para ejecutarla y puede ser usada en una función."""
    return accion

def no(valor):
    """Devuelve el valor contrario de un booleano."""
    return not valor

def ó(*valores):
    """Funciona como un or para múltiples valores."""
    return any(valores)

def y(*valores):
    """Funciona como un and para múltiples valores."""
    return all(valores)

def intentar(intento, errores, retorno):
    """Intenta ejecutar una función y si hay un error, se maneja con una excepción."""
    try:
        resultado = intento()
    except errores as e:
        print(f"Ocurrió una excepción: {e}")
        return retorno
    else:
        return resultado

def importar(modulo):
    """Importa un módulo dentro de una variable, la variable funcionará como el alias con el cual se llamará al módulo."""
    return importlib.import_module(modulo)

def para(iterable, funcion):
    """Hace un funcionamiento parecido a un bucle for."""
    iterator = iter(iterable)
    while True:
        try:
            elemento = next(iterator)
            funcion(elemento)
        except StopIteration:
            break

def es(valor1, valor2):
    """Compara si dos valores son lo mismo."""
    return valor1 is valor2

def no_es(valor1, valor2):
    """Compara si dos valores no son lo mismo."""
    return valor1 is not valor2

def ent(valor):
    """Convierte una cadena o un decimal a entero teniendo en cuenta las normas de int()"""
    return int(valor)

def decim(valor):
    """Convierte una cadena o un entero a decimal teniendo en cuenta las normas de float()"""
    return float(valor)

def cad(valor):
    """Convierte un entero o un decimal a cadena teniendo en cuenta las normas de str()"""
    return str(valor)

def redondear(numero, decimales):
    """Redondea un número usando round de python."""
    return round(numero, decimales)

def descargar(url):
    """Descarga un archivo usando curl, si no tiene curl en su sistema, debe instalarlo, si quiere verificar que curl este instalado puede usar curl --version en un terminal."""
    comando = subprocess.run(f"curl -L {url}", shell= True, check=True)
    return comando
