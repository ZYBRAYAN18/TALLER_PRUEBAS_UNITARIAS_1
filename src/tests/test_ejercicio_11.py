import pytest
from src.ejercicio_11 import division_segura


def test_division_exacta():
    # Arrange
    dividendo = 10
    divisor = 2
    esperado = 5.0

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_periodica_precision_flotante():
    # Arrange
    dividendo = 10
    divisor = 3
    esperado = pytest.approx(3.3333, rel=1e-3)

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_cero_en_dividendo():
    # Arrange
    dividendo = 0
    divisor = 5
    esperado = 0.0

    # Act
    resultado = division_segura(dividendo, divisor)

    # Assert
    assert resultado == esperado


def test_division_por_cero_lanza_zero_division_error():
    # Arrange
    dividendo = 8
    divisor = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError, match="No es posible dividir entre cero"):
        division_segura(dividendo, divisor)