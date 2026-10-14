import pytest
from src.ejercicio_09 import es_palindromo


def test_es_palindromo_palabra_simple():
    # Arrange
    cadena = "radar"
    esperado = True

    # Act
    resultado = es_palindromo(cadena)

    # Assert
    assert resultado is esperado


def test_es_palindromo_frase_con_espacios_y_mayusculas():
    # Arrange
    cadena = "Anita lava la tina"
    esperado = True

    # Act
    resultado = es_palindromo(cadena)

    # Assert
    assert resultado is esperado


def test_es_palindromo_palabra_no_palindroma():
    # Arrange
    cadena = "Sofware"
    esperado = False

    # Act
    resultado = es_palindromo(cadena)

    # Assert
    assert resultado is esperado


def test_es_palindromo_cadena_solo_espacios():
    # Arrange
    cadena = "   "
    esperado = False

    # Act
    resultado = es_palindromo(cadena)

    # Assert
    assert resultado is esperado


def test_es_palindromo_tipo_numerico_lanza_type_error():
    # Arrange
    entrada_invalida = 1001

    # Act & Assert
    with pytest.raises(TypeError, match="El parámetro debe ser una cadena de texto"):
        es_palindromo(entrada_invalida)