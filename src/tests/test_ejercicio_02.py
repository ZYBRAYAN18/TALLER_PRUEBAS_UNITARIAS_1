import pytest
from src.ejercicio_02 import es_par


# 1. Caso positivo con número par positivo (ej. 8)
def test_es_par_con_numero_par_positivo():
    # Arrange
    numero = 8
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado == esperado


# 2. Caso negativo con número impar positivo (ej. 7)
def test_es_par_con_numero_impar_positivo():
    # Arrange
    numero = 7
    esperado = False

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado == esperado


# 3. Comportamiento en el valor neutro 0 (matemáticamente par)
def test_es_par_con_valor_neutro_cero():
    # Arrange
    numero = 0
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado == esperado


# 4. Comportamiento con enteros negativos pares e impares (ej. -4 y -9)
def test_es_par_con_entero_negativo_par():
    # Arrange
    numero = -4
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado == esperado


def test_es_par_con_entero_negativo_impar():
    # Arrange
    numero = -9
    esperado = False

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado == esperado


# 5. Rechazo con TypeError si se ingresa un número decimal (4.0)
def test_es_par_lanza_type_error_con_decimal():
    # Arrange
    numero_decimal = 4.0

    # Act & Assert
    with pytest.raises(TypeError):
        es_par(numero_decimal)