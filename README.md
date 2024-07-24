# Problemas-de-Sincronización
Este proyecto tiene como objetivo mostrar la solución de algunos problemas clásicos de sincronización utilizando la librería "multiprocessing". La idea es mostrar de forma gráfica como funciona estos problemas, debido a que internamente estos problemas pasan desapercibido.

## 1 - Filósofos Comensales
La situación se plantea de la siguiente manera: Hay 5 filósofos sentados
alrededor de una mesa redonda, cada uno con un plato de espaguetis frente
a él. Entre cada par de filósofos hay un tenedor que deben compartir para
poder comer. Los filósofos pasan la mayor parte del tiempo pensando, pero
de vez en cuando tienen hambre y deben comer, lo que requiere tomar los
dos tenedores que están a sus lados.

![Texto alternativo](1-filosofos_hambrientos/assets/ejemplo1.png)

### Solución
El problema radica en coordinar el acceso a los tenedores de manera que
ningún filósofo se quede esperando indefinidamente por los tenedores que
necesita para comer.
Este problema tiene diversas formas de solucionarse, tomando la solución
paralela del mismo(Teniendo en cuenta que puede ejecutar múltiples
procesos a la vez) podemos deducir que para 5 filósofos en el mejor de los
casos solo 2 filósofos podrán comer a la vez.

## 2 - Lectores Escritores
La situación se plantea de la siguiente manera: Existe un recurso
compartido, por ejemplo, una base de datos o un archivo, al cual pueden
acceder simultáneamente múltiples procesos. Algunos de estos procesos
son escritores, que necesitan modificar el contenido del recurso, mientras
que otros son lectores, que solo requieren leer el contenido sin alterarlo.

### Solución
Para solucionar este problema podemos emplear 2 semáforos para
controlar la actividad tanto de los lectores como los escritores. Teniendo en
cuenta las reglas mencionadas antes donde los escritores tienen prioridad y
escritores y lectores no pueden trabajar al mismo tiempo.

# Como Ejecutar
Para ejecutar sería tan sencillo como clonar el repositorio, instalar las siguientes dependencias y por cada carpeta existe un archivo run.bat que permite la ejecución directa del programa.

### Dependencias
```python
pip install multiprocessing
pip install pillow
```


