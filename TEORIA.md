SM-1 = C ; A no es porque shift-left es probar desde el principio, justo lo contrario a dejar las pruebas al final ; B no es porque shift-right son pruebas que se hacen en producción con usuarios reales, no probar al final ; D no es porque integración continua es subir el código seguido al repo, no tiene que ver con cuándo se diseñan las pruebas.

SM-2 = B ; A no es porque refactor solo se hace cuando los tests ya están en verde, no antes de escribir código ; C no es porque el Green es hacer el código mínimo para pasar un test que ya existe, y aquí ni siquiera había test ; D no es porque en TDD primero va el test que falla y después el código, no al revés.

pa-1

TDD pide en el GREEN el código más simple aunque se vea feo porque lo único que importa en ese paso es que el test pase. Si uno se pone a escribir código bonito desde el inicio, termina metiendo cosas que ningún test pidió y se pierde la idea de que cada línea esté ahí por una razón. También se salta el REFACTOR, que es donde se limpia el código tranquilo porque los tests cuidan que nada se rompa. Si se mezclan las fases se pierde el orden, aparecen funciones sin prueba y se daña la red de seguridad que da TDD. Por eso primero feo y después limpio.

pa-2

TDD nace para ayudar al programador a escribir mejor código, lo hace ir paso a paso: primero el test y después la solución, así no mete cosas de más y puede cambiar el código sin miedo. BDD en cambio nace para que todo el equipo entienda lo mismo que el cliente, usa frases en lenguaje normal para decir cómo debería comportarse el sistema. TDD es más para los que programan y BDD para todos, incluso los que no son técnicos. No se reemplazan porque sirven para cosas distintas: BDD ayuda a ponerse de acuerdo en qué hacer y TDD ayuda a hacerlo bien por dentro.