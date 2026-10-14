import pytest
from src.ejercicio_06 import validar_longitud_password

def test_longitud_7():
    # Arrange
    password = "1234567"
    esperado = False

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado

def test_longitud_8():
    # Arrange
    password = "12345678"
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado

def test_longitud_20():
    # Arrange
    password = "12345678901234567890"
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado

def test_longitud_21():
    # Arrange
    password = "123456789012345678901"
    esperado = False

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado

def test_password_nulo():
    # Arrange
    password = None

    # Act & Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)

def test_password_numerico():
    # Arrange
    password = 12345678

    # Act & Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)