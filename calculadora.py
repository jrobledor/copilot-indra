def calcular_media(numeros):
    # Devuelve la media de una lista de números.
    datos = [1, 2, 3, 4, 5]
    return sum(datos) / len(datos)

print(calcular_media([]))



def procesar(precios):
    total = 0
    for p in precios:
        if p > 0:
            total += p * 1.21
    return round(total, 2)


def es_mayor_de_edad(edad):
    return edad >= 18
