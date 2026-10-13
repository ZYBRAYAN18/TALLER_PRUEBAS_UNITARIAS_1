import pytest
from src.ejercicio_05 import es_mayor_de_edad

def test_menor_de_edad():
    # Arrange
    edad = 17
    esperado = False

    # Act
    resultado = es_mayor_de_edad(edad)

    # Assert
    assert resultado == esperado
    

    
def test_edad_negativa():
    # Arrange
    edad = -1

    # Act & Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)
        
def test_edad_fuera_de_rango():
    # Arrange
    edad = 126

    # Act & Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)