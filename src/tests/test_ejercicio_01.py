import pytest
# Ajusta la ruta de importación según cómo se llame tu archivo en src
from src.ejercicio_01 import sumar


# 1. Happy Path: Suma de dos enteros positivos (2 + 3 = 5)
def test_suma_dos_enteros_positivos():
    # Arrange
    num1 = 2
    num2 = 3
    esperado = 5

    # Act
    resultado = sumar(num1, num2)

    # Assert
    assert resultado == esperado


# 2. Suma con negativos: Un entero positivo y un negativo (10 + (-4) = 6)
def test_suma_positivo_y_negativo():
    # Arrange
    num1 = 10
    num2 = -4
    esperado = 6

    # Act
    resultado = sumar(num1, num2)

    # Assert
    assert resultado == esperado


# 3. Manejo de tipos inválidos: TypeError con string ("5")
def test_lanzamiento_type_error_con_string():
    # Arrange
    arg_invalido = "5"
    arg_valido = 3

    # Act & Assert
    with pytest.raises(TypeError):
        sumar(arg_invalido, arg_valido)


# 4. Manejo de booleanos: TypeError con booleano (True)
def test_lanzamiento_type_error_con_booleano():
    # Arrange
    arg_booleano = True
    arg_valido = 5

    # Act & Assert
    with pytest.raises(TypeError):
        sumar(arg_booleano, arg_valido)