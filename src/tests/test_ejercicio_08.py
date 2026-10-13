import pytest
from src.ejercicio_08 import obtener_mayor


def test_obtener_mayor_enteros_positivos_desordenados():
    # Arrange
    lista = [4, 12, 8, 3]
    esperado = 12

    # Act
    resultado = obtener_mayor(lista)
    
    # Assert
    assert resultado == esperado

    # Arrange
def test_obtener_mayor_numeros_negativos():
    lista = [-15, -3, -8, -20]
    esperado = -3

    # Act
    resultado = obtener_mayor(lista)

    # Assert
    assert resultado == esperado


def test_obtener_mayor_un_unico_elemento():
    # Arrange
    lista = [42]
    esperado = 42

    # Act
    resultado = obtener_mayor(lista)

    # Assert
    assert resultado == esperado


def test_obtener_mayor_lista_vacia_lanza_value_error():
    # Arrange
    lista_vacia = []

    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        obtener_mayor(lista_vacia)


def test_obtener_mayor_elementos_corruptos_lanza_type_error():
    # Arrange
    lista_corrupta = [1, 2, "tres"]

    # Act & Assert
    with pytest.raises(TypeError, match="Todos los elementos de la lista deben ser números"):
        obtener_mayor(lista_corrupta)