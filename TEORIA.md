SM-1 = C ; A no es porque shift-left es probar desde el principio, justo lo contrario a dejar las pruebas al final ; B no es porque shift-right son pruebas que se hacen en producción con usuarios reales, no probar al final ; D no es porque integración continua es subir el código seguido al repo, no tiene que ver con cuándo se diseñan las pruebas.

SM-2 = B ; A no es porque refactor solo se hace cuando los tests ya están en verde, no antes de escribir código ; C no es porque el Green es hacer el código mínimo para pasar un test que ya existe, y aquí ni siquiera había test ; D no es porque en TDD primero va el test que falla y después el código, no al revés.

pa-1

TDD pide en el GREEN el código más simple aunque se vea feo porque lo único que importa en ese paso es que el test pase. Si uno se pone a escribir código bonito desde el inicio, termina metiendo cosas que ningún test pidió y se pierde la idea de que cada línea esté ahí por una razón. También se salta el REFACTOR, que es donde se limpia el código tranquilo porque los tests cuidan que nada se rompa. Si se mezclan las fases se pierde el orden, aparecen funciones sin prueba y se daña la red de seguridad que da TDD. Por eso primero feo y después limpio.

pa-2

TDD nace para ayudar al programador a escribir mejor código, lo hace ir paso a paso: primero el test y después la solución, así no mete cosas de más y puede cambiar el código sin miedo. BDD en cambio nace para que todo el equipo entienda lo mismo que el cliente, usa frases en lenguaje normal para decir cómo debería comportarse el sistema. TDD es más para los que programan y BDD para todos, incluso los que no son técnicos. No se reemplazan porque sirven para cosas distintas: BDD ayuda a ponerse de acuerdo en qué hacer y TDD ayuda a hacerlo bien por dentro.

pa-3

Tener mucha cobertura solo quiere decir que los tests pasaron por casi todas las líneas, pero no quiere decir que se hayan probado bien ni que se haya revisado si el resultado era el correcto. Por ejemplo, una función que suma puede tener un test que la corra con 2 y 2, pero si el test nunca revisa que el resultado sea 4, podría dar 100 y el test pasaría igual. La cobertura cuenta líneas que se ejecutaron, no errores que se encontraron. Pueden faltar casos raros o valores en los bordes, así que tener 95% no quiere decir que no haya bugs, solo dice que el código se ejecutó.

pa-4

Lo que dice el compañero está mal porque probar solo un valor del medio no revisa qué pasa en los bordes, que es donde más se equivoca uno con los signos de mayor o menor. Si el código dice "menor que 40" cuando debería decir "menor o igual a 40", el test con 20% nunca lo va a notar. Yo probaría valores como 0% y 40% que son los bordes que sí valen, 1% y 39% que están justo adentro, y -1% y 41% que están justo afuera. Así me aseguro que el sistema acepte lo que tiene que aceptar y rechace lo que tiene que rechazar.

pa-5

Un pipeline de CI/CD funciona corriendo los tests solo cada vez que alguien sube código, y si todo pasa, el cambio se integra o se sube a producción. TDD y BDD son las prácticas que hacen esos tests: TDD hace que cada parte del código tenga su prueba chiquita y rápida, y BDD hace que el comportamiento que pide el negocio también esté probado. Si no hay buenos tests, el pipeline pierde sentido porque estaría integrando y subiendo cosas sin saber si algo se dañó. Sería como una banda muy rápida llevando cosas al cliente sin nadie revisando si están bien.
