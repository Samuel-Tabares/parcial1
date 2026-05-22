# language: es

Característica: Calcular el precio final de los productos de la libreria
  Como administrador de la libreria
  Quiero aplicar descuentos a los productos y ver el precio final con IVA
  Para vender los productos al precio correcto

  Antecedentes:
    Dado que tengo un producto que cuesta 10000

  @regla2 @positivo
  Escenario: Aplicar un descuento valido
    Cuando aplico un descuento del 20%
    Entonces el precio queda en 8000

  @regla2 @error
  Escenario: No se puede aplicar un descuento mayor al permitido
    Cuando intento aplicar un descuento del 50%
    Entonces el sistema me debe rechazar

  @regla2 @bordes
  Esquema del escenario: Probar los bordes del descuento
    Cuando aplico un descuento del <porcentaje>%
    Entonces el precio queda en <resultado>

    Ejemplos:
      | porcentaje | resultado |
      | 0          | 10000     |
      | 40         | 6000      |

  @regla3 @positivo
  Escenario: Calcular el precio final con descuento y IVA
    Cuando pido el precio final con un descuento del 10%
    Entonces el precio final es 10710

  @regla3 @positivo
  Escenario: Calcular el precio final sin descuento
    Cuando pido el precio final con un descuento del 0%
    Entonces el precio final es 11900
