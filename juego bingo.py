import random
import time

def sortear_numeros(inicio, fin, cantidad):
    # comprueba que la cantidad no supere el rango disponible
    rango_total = fin - inicio + 1
    if cantidad > rango_total:
        print(f"Error: No se pueden sortear {cantidad} números entre {inicio} y {fin}.")
        return

    # Crea la lista de números y la mezcla
    numeros = list(range(inicio, fin + 1))
    random.shuffle(numeros)

    print(f"\nSorteando {cantidad} número(s) entre {inicio} y {fin}...\n")
    time.sleep(1)

    # Sortea y muestra los resultados
    for i in range(cantidad):
        numero = numeros.pop()
        print(f"Número sorteado: {numero}")
        time.sleep(1)

# Bloque principal
if __name__ == "__main__":
    print("---- Sorteo de Números ----")
    try:
        inicio = int(input("Ingresa el número inicial del sorteo: "))
        fin = int(input("Ingresa el número final del sorteo: "))
        cantidad = int(input("¿Cuántos números queres sortear?: "))

        sortear_numeros(inicio, fin, cantidad)

    except ValueError:
        print("Error: Debes ingresar solo números enteros.") 
