# tests de la Regla 1: el producto tiene nombre y precio y el precio debe ser mayor que cero
import pytest
from producto import Producto


def test_crear_producto_con_precio_valido():
    # si paso un precio bueno el producto se debe crear bien
    p = Producto("libro", 5000)
    assert p.nombre == "libro"
    assert p.precio == 5000


def test_no_se_puede_crear_producto_con_precio_cero():
    # si el precio es 0 debe salir error
    with pytest.raises(ValueError):
        Producto("libro", 0)


def test_no_se_puede_crear_producto_con_precio_negativo():
    # si el precio es negativo tambien debe salir error
    with pytest.raises(ValueError):
        Producto("libro", -100)
