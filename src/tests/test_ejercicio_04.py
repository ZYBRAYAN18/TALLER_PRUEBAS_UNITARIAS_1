import pytest
from src.ejercicio_04 import aplicar_descuento

def test_descuento_valido():
    # Arrange
    precio = 100
    porcentaje_descuento = 20
    esperado = 80

    # Act
    resultado = aplicar_descuento(precio, porcentaje_descuento)

    # Assert
    assert resultado == esperado
    
def test_descuento_cero():
    # Arrange
    precio = 50
    porcentaje_descuento = 0
    esperado = 50

    # Act
    resultado = aplicar_descuento(precio, porcentaje_descuento)

    # Assert
    assert resultado == esperado
    
def test_descuento_cien_por_ciento():
    # Arrange
    precio = 75
    porcentaje_descuento = 100
    esperado = 0

    # Act
    resultado = aplicar_descuento(precio, porcentaje_descuento)

    # Assert
    assert resultado == esperado
    
def test_precio_negativo():
    # Arrange
    precio = -1
    porcentaje_descuento = 0

    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje_descuento)
        
def test_descuento_fuera_de_rango():
    # Arrange
    precio = 100
    porcentaje_descuento = 101

    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje_descuento)