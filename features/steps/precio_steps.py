# step definitions del archivo precio.feature, conectan los escenarios con la clase Producto
from behave import given, when, then
import sys
import os

# agregamos la carpeta src para poder importar la clase Producto
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from producto import Producto


@given('que tengo un producto que cuesta {precio:d}')
def step_tengo_producto(context, precio):
    # guardamos el producto y limpiamos resultado y error para empezar limpio
    context.producto = Producto("libro", precio)
    context.resultado = None
    context.error = None


@when('aplico un descuento del {porcentaje:d}%')
def step_aplicar_descuento(context, porcentaje):
    # intentamos aplicar el descuento, si sale error lo guardamos para revisar despues
    try:
        context.resultado = context.producto.aplicar_descuento(porcentaje)
    except ValueError as e:
        context.error = e


@when('intento aplicar un descuento del {porcentaje:d}%')
def step_intento_aplicar_descuento(context, porcentaje):
    # mismo de arriba pero la frase es "intento" para los casos de error
    try:
        context.resultado = context.producto.aplicar_descuento(porcentaje)
    except ValueError as e:
        context.error = e


@when('pido el precio final con un descuento del {porcentaje:d}%')
def step_calcular_precio_final(context, porcentaje):
    # calculamos el precio final aplicando descuento y despues IVA
    context.resultado = context.producto.calcular_precio_final(porcentaje)


@then('el precio queda en {esperado:d}')
def step_precio_queda(context, esperado):
    # revisamos que el precio sea el esperado
    assert context.resultado == esperado


@then('el precio final es {esperado:d}')
def step_precio_final(context, esperado):
    # revisamos que el precio final con IVA sea el esperado
    assert context.resultado == esperado


@then('el sistema me debe rechazar')
def step_rechaza(context):
    # verificamos que si haya salido un error de validacion
    assert context.error is not None
