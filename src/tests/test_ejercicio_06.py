import pytest
from src.ejercicio_06 import  validar_longitud_password

def test_password_en_limite_inferior():
    # Arrange
    password = "hola1234"  
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado

    
def test_password_en_limite_superior():
    # Arrange
    password = "contraseñasegura12345678" * 2  # 20 caracteres
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado == esperado


