# 🐵 Juego de Chango y Bananas Matemáticas 🍌
Este es un juego de matemáticas interactivo, donde un mono debe atrapar bananas que contienen soluciones correctas a ecuaciones cuadráticas. Las bananas caen desde la parte superior de la pantalla y el jugador debe mover el mono para recoger las soluciones correctas, ¡evitando los números falsos!   ![Image Alt](image_url)

# 📝 Descripción del Juego
En este juego educativo, el objetivo es ayudar al mono a resolver ecuaciones cuadráticas capturando bananas con soluciones correctas. Cada ronda, se genera una ecuación aleatoria y dos soluciones, una de las cuales es falsa para aumentar el reto. El jugador debe moverse con las teclas de dirección para capturar la banana correcta, obteniendo un punto por cada acierto. 

# 🚀 Ejecución
Para ejecutar el juego, asegúrate de tener instalados los módulos pygame, sympy, y matplotlib :
```bash
pip install pygame sympy matplotlib
```
```bash
python nombre_del_archivo.py
```

# Funcionamiento del Juego
`Generación de Ecuación`: En cada ronda, se crea una ecuación cuadrática aleatoria usando la biblioteca `sympy`. Se genera una imagen de la ecuación para mostrarla en pantalla.

Imagen: ecuacion.png (Imagen de la ecuación generada).  ![Image Alt](https://github.com/eggar284/bannnaGame/blob/main/ecuacion.png?raw=true)

`Soluciones Correctas y Falsas`: Se calculan las soluciones reales de la ecuación. A continuación, se crean números falsos que no sean soluciones para aumentar el nivel de dificultad.

Imagen: solucion_X.png (Banana con la solución correcta).
Imagen: falso_X.png (Banana con un número incorrecto).

`Interacción con el Jugador`: El mono puede moverse hacia la izquierda y derecha para atrapar las bananas. Si atrapa una banana con la solución correcta, gana un punto y se genera una nueva ecuación. Si atrapa un número falso o se pierde una solución válida, el juego termina.

Imagen: monito_atrapando_banana_correcta.png (El mono atrapa una banana con la solución correcta).
Imagen: monito_perdiendo.png (El jugador pierde por atrapar una banana incorrecta o dejar caer una correcta).

# Estructura del Código

`limpiar_imagenes()`: Elimina imágenes de soluciones anteriores al inicio del juego para evitar conflictos.

`generar_imagen_ecuacion(ecuacion)`: Genera una imagen de la ecuación actual usando matplotlib.

`resolver_ecuacion()`: Calcula las soluciones de la ecuación generada y almacena las soluciones correctas.

`generar_imagen_solucion(solucion, filename)`: Genera una imagen de la solución específica que será usada como banana en el juego.

`actualizar_imagenes(soluciones, falsos)`: Actualiza la lista de imágenes de las bananas (soluciones y números falsos) para la ronda actual.


`juego()`: Ejecuta el bucle principal del juego, gestiona los movimientos del mono, genera nuevas bananas, y verifica las colisiones con el mono.

# Control del Juego

Usa las teclas de dirección Izquierda y Derecha para mover el mono.

Atrapa las bananas con la solución correcta para ganar puntos.

Evita las bananas con números incorrectos para no perder.


Imágenes y Ejemplos
`Pantalla Inicial con Ecuación`: En esta pantalla, se muestra la ecuación actual que el jugador debe resolver.

Imagen de ejemplo: ecuacion_mostrada.png
`Banana Correcta`: Esta imagen muestra la banana con la solución correcta. Al atraparla, el jugador gana un punto.

Imagen de ejemplo: banana_correcta.png
Banana Falsa: La imagen de esta banana contiene un número incorrecto. Atrapar esta banana hace que el jugador pierda.

Imagen de ejemplo: banana_falsa.png
Puntos Acumulados: En la parte superior de la pantalla, se muestra el puntaje acumulado del jugador. El jugador debe intentar obtener la mayor cantidad de puntos posible.

Imagen de ejemplo: puntaje_acumulado.png
Mono Moviéndose: Esta imagen muestra al mono moviéndose hacia la izquierda y derecha para atrapar bananas.

Imagen de ejemplo: mono_movimiento.png
