# clase Producto: guarda nombre y precio, valida el precio y aplica descuentos
class Producto:
    def __init__(self, nombre, precio):
        # llamamos al metodo que valida el precio antes de guardarlo
        self._validar_precio(precio)
        self.nombre = nombre
        self.precio = precio

    def _validar_precio(self, precio):
        # si el precio no es mayor que cero no dejamos crear el producto
        if precio <= 0:
            raise ValueError("el precio debe ser mayor que cero")

    def _validar_descuento(self, porcentaje):
        # el descuento debe estar entre 0 y 40, si no se rechaza
        if porcentaje < 0 or porcentaje > 40:
            raise ValueError("el descuento debe estar entre 0% y 40%")

    def aplicar_descuento(self, porcentaje):
        # primero validamos y despues calculamos
        self._validar_descuento(porcentaje)
        descuento = self.precio * porcentaje / 100
        return self.precio - descuento
