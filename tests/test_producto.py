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


# tests de la Regla 2: el descuento debe estar entre 0% y 40%

def test_aplicar_descuento_del_20_porciento():
    # 20% de 10000 es 2000, entonces queda en 8000
    p = Producto("libro", 10000)
    assert p.aplicar_descuento(20) == 8000


def test_aplicar_descuento_del_0_porciento():
    # el 0% es valido y no quita nada, queda igual
    p = Producto("libro", 10000)
    assert p.aplicar_descuento(0) == 10000


def test_aplicar_descuento_del_40_porciento():
    # 40% es el maximo permitido, 40% de 10000 son 4000, queda en 6000
    p = Producto("libro", 10000)
    assert p.aplicar_descuento(40) == 6000


def test_no_se_puede_aplicar_descuento_mayor_a_40():
    # un descuento de 50% debe ser rechazado
    p = Producto("libro", 10000)
    with pytest.raises(ValueError):
        p.aplicar_descuento(50)


def test_no_se_puede_aplicar_descuento_negativo():
    # un descuento negativo tambien debe ser rechazado
    p = Producto("libro", 10000)
    with pytest.raises(ValueError):
        p.aplicar_descuento(-5)
