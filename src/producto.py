# clase Producto: guarda nombre y precio, valida el precio, aplica descuentos y calcula el precio final
class Producto:
    # el IVA en colombia es del 19%, lo dejamos como constante para no tener un numero suelto
    IVA = 0.19

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

    def calcular_precio_final(self, porcentaje_descuento):
        # primero se aplica el descuento y despues se le suma el IVA
        precio_con_descuento = self.aplicar_descuento(porcentaje_descuento)
        precio_final = precio_con_descuento * (1 + self.IVA)
        return precio_final
