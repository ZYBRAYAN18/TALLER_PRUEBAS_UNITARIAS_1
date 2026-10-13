import pytest
from src.ejercicio_03 import celsius_a_fahrenheit

def test_punto_congelacion_agua():
    #Arrange
    celsius = 0
    esperado = 32

    #Act
    resultado = celsius_a_fahrenheit(celsius)

    #Assert
    assert resultado == esperado
    
def test_punto_ebullicion_agua():
    #Arrange
    celsius = 100
    esperado = 212      
    
    #Act
    resultado = celsius_a_fahrenheit(celsius)

    #Assert
    assert resultado == esperado    

def test_coincidencia_de_escalas():
    #Arrange
    celsius = -40
    esperado = -40      
    
    #Act
    resultado = celsius_a_fahrenheit(celsius)

    #Assert
    assert resultado == esperado
    
def test_precision_decimal():
    #Arrange
    celsius = 37.5
    esperado = 99.5      
    
    #Act
    resultado = celsius_a_fahrenheit(celsius)

    #Assert
    assert resultado == esperado
    
def test_limite_inferior_no_permitido():
    #Arrange
    celsius = -300

    #Act & Assert
    with pytest.raises(ValueError):
        celsius_a_fahrenheit(celsius)
    