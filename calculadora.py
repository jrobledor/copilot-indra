def calcular_media(valores):
    """Devuelve la media de una lista de números."""
    if not valores:
        return 0.0

    return sum(valores) / len(valores)


def procesar(precios):
    """Calcula el total con IVA del 21% para los precios positivos."""
    total = 0.0

    for precio in precios:
        if precio > 0:
            total += precio * 1.21

    return float(round(total, 2))


def es_mayor_de_edad(edad):
    """Devuelve True si la persona es mayor de edad."""
    if not isinstance(edad, (int, float)):
        raise TypeError("La edad debe ser un número.")

    return edad >= 18
