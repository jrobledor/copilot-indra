import pytest

from calculadora import calcular_media, es_mayor_de_edad, procesar


@pytest.mark.parametrize(
    ("lista_de_numeros", "resultado_esperado"),
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30], 20.0),
        ([], 0.0),
    ],
)
def test_calcular_media_con_numeros(lista_de_numeros, resultado_esperado):
    assert calcular_media(lista_de_numeros) == resultado_esperado


@pytest.mark.parametrize(
    ("precios", "resultado_esperado"),
    [
        ([10, 20, 30], 72.6),
        ([100, -5, 50], 181.5),
        ([], 0.0),
    ],
)
def test_procesar_aplica_iva_a_precios_positivos(precios, resultado_esperado):
    assert procesar(precios) == resultado_esperado


@pytest.mark.parametrize(
    ("edad", "resultado_esperado"),
    [
        (17, False),
        (18, True),
        (19, True),
        (-1, False),
    ],
)
def test_es_mayor_de_edad_con_numeros(edad, resultado_esperado):
    assert es_mayor_de_edad(edad) is resultado_esperado


@pytest.mark.parametrize("edad", ["18", None])
def test_es_mayor_de_edad_rechaza_valores_no_numericos(edad):
    with pytest.raises(TypeError):
        es_mayor_de_edad(edad)