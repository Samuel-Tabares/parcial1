# clase Producto, por ahora solo guarda nombre y precio y revisa que el precio sea mayor que cero
class Producto:
    def __init__(self, nombre, precio):
        # si el precio no es mayor que cero no dejamos crear el producto
        if precio <= 0:
            raise ValueError("el precio debe ser mayor que cero")
        self.nombre = nombre
        self.precio = precio
