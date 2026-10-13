import pytest
from src.ejercicio_07 import factorial

def test_factorial_caso_base_cero():
    # Arrange
    n = 0
    esperado = 1

    # Act
    resultado = factorial(n)

    # Assert
    assert resultado == esperado


def test_factorial_caso_base_uno():
    # Arrange
    n = 1
    esperado = 1

    # Act
    resultado = factorial(n)

    # Assert
    assert resultado == esperado


def test_factorial_caso_tipico_cinco():
    # Arrange
    n = 5
    esperado = 120

    # Act
    resultado = factorial(n)

    # Assert
    assert resultado == esperado


def test_factorial_numero_mayor_siete():
    # Arrange
    n = 7
    esperado = 5040

    # Act
    resultado = factorial(n)

    # Assert
    assert resultado == esperado


def test_factorial_numero_negativo_lanza_value_error():
    # Arrange
    n = -3

    # Act & Assert
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
        factorial(n)