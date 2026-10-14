import pytest
from src.ejercicio_12 import procesar_usuario


def test_procesar_usuario_caso_exitoso():
    # Arrange
    datos_entrada = {"id": 1, "nombre": "Carlos Pérez", "activo": True}
    esperado = {
        "id": 1,
        "nombre": "Carlos Pérez",
        "activo": True,
        "estado_registro": "VALIDADO",
    }

    # Act
    resultado = procesar_usuario(datos_entrada)

    # Assert
    assert resultado == esperado
    assert "estado_registro" in resultado
    assert resultado["id"] == 1
    assert resultado["nombre"] == "Carlos Pérez"
    assert resultado["activo"] is True


def test_procesar_usuario_clave_faltante_lanza_value_error():
    # Arrange
    datos_incompletos = {"id": 1, "nombre": "Carlos Pérez"}  # Falta "activo"

    # Act & Assert
    with pytest.raises(ValueError, match="Faltan campos requeridos en el registro"):
        procesar_usuario(datos_incompletos)


def test_procesar_usuario_id_invalido_cero_o_negativo_lanza_value_error():
    # Arrange
    datos_id_cero = {"id": 0, "nombre": "Carlos Pérez", "activo": True}
    datos_id_negativo = {"id": -5, "nombre": "Carlos Pérez", "activo": True}

    # Act & Assert
    with pytest.raises(ValueError, match="El id debe ser un entero positivo mayor a cero"):
        procesar_usuario(datos_id_cero)

    with pytest.raises(ValueError, match="El id debe ser un entero positivo mayor a cero"):
        procesar_usuario(datos_id_negativo)


def test_procesar_usuario_nombre_vacio_o_espacios_lanza_value_error():
    # Arrange
    datos_nombre_vacio = {"id": 1, "nombre": "   ", "activo": True}

    # Act & Assert
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía"):
        procesar_usuario(datos_nombre_vacio)


def test_procesar_usuario_argumento_no_diccionario_lanza_type_error():
    # Arrange
    entrada_invalida = ["id", "nombre", "activo"]

    # Act & Assert
    with pytest.raises(TypeError, match="El parámetro debe ser un diccionario"):
        procesar_usuario(entrada_invalida)