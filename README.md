Parcial de Pruebas de Software, calcula el precio final de los productos de una libreria, siguiendo las tres reglas que dio el administrador

Para correr el proyecto toca crear un entorno virtual con 
python3 -m venv venv
activarlo con 
source venv/bin/activate 
y despues instalar los requirements con 
pip install -r requirements.txt
Los tests se corren con pytest.

La carpeta src es donde va el codigo y la carpeta tests es donde van las pruebas.

Analisis antes de programar

Particiones de equivalencia de la Regla 1 (precio base debe ser mayor que cero)

```
Particion              Valida   Valor   Resultado esperado
precio mayor que 0     si       5000    el producto se crea bien
precio igual a 0       no       0       el sistema lo rechaza
precio negativo        no       -200    el sistema lo rechaza
```

Particiones de equivalencia de la Regla 2 (descuento entre 0% y 40%)

```
Particion                   Valida   Valor   Resultado esperado
descuento entre 0 y 40      si       20      se aplica el descuento
descuento menor que 0       no       -5      el sistema lo rechaza
descuento mayor a 40        no       55      el sistema lo rechaza
```

Valores limite de la Regla 2 (los bordes del rango 0 a 40)

```
Valor   Valido   Resultado esperado
-1      no       el sistema lo rechaza
0       si       se acepta, no quita nada
1       si       se acepta
39      si       se acepta
40      si       se acepta, es el maximo
41      no       el sistema lo rechaza
```

Pregunta para el administrador sobre la Regla 3

Cuando el precio final tenga decimales, se redondea o se deja con los decimales? Esto importa porque segun la respuesta cambia el resultado esperado de los tests y no se puede comparar bien si no se sabe.
