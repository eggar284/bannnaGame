import pygame
import sys
import random
import sympy as sp
import matplotlib.pyplot as plt
import os

# Eliminar archivos de imágenes existentes al inicio del juego
def limpiar_imagenes():
    for archivo in os.listdir():
        if archivo.startswith("solucion_") and archivo.endswith(".png"):
            os.remove(archivo)
        elif archivo.startswith("falso_") and archivo.endswith(".png"):
            os.remove(archivo)

limpiar_imagenes()

# Función para generar imagen de la ecuación
def generar_imagen_ecuacion(ecuacion):
    if os.path.exists('ecuacion.png'):
        os.remove('ecuacion.png')
    plt.figure(figsize=(2, .5))
    plt.text(0.5, 0.5, f'${sp.latex(ecuacion)}$', fontsize=15, ha='center', va='center')
    plt.axis('off')
    plt.savefig('ecuacion.png', bbox_inches='tight', pad_inches=0.1)
    plt.close()

# Calcula las soluciones
def resolver_ecuacion():
    global ecuacion, soluciones
    a = random.randint(1, 10)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    while b**2 - 4*a*c < 0:
        c = random.randint(-9, 9)

    x = sp.Symbol('x')
    ecuacion = a*x**2 + b*x + c
    soluciones = sp.solve(ecuacion, x)
    soluciones = [sp.nsimplify(sol) for sol in soluciones]
    
    generar_imagen_ecuacion(ecuacion)
    
    return soluciones

# Genera imágenes de las soluciones
def generar_imagen_solucion(solucion, filename):
    plt.figure(figsize=(1, 0.5))
    texto = sp.latex(solucion)
    plt.text(0.5, 0.5, f'${texto}$', fontsize=10, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.05)
    plt.close()

# Mostrar texto
def mostrar_texto(texto, x, y, color=(255, 255, 255), tamaño=30):
    font = pygame.font.Font(None, tamaño)
    superficie_texto = font.render(texto, True, color)
    rect_texto = superficie_texto.get_rect(center=(x, y))
    screen.blit(superficie_texto, rect_texto)

# Función para actualizar imágenes de soluciones y falsos
def actualizar_imagenes(soluciones, falsos):
    for i, sol in enumerate(soluciones):
        generar_imagen_solucion(sol, f'solucion_{i}.png')
    for i, falso in enumerate(falsos):
        generar_imagen_solucion(falso, f'falso_{i}.png')

    imagenes_bananas = []
    for i in range(len(soluciones)):
        imagenes_bananas.append(pygame.image.load(f'solucion_{i}.png'))
    for i in range(len(falsos)):
        imagenes_bananas.append(pygame.image.load(f'falso_{i}.png'))
    return imagenes_bananas

def juego():
    global screen
    pygame.init()
    screen = pygame.display.set_mode([360, 640])

    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)

    background_image = pygame.image.load(r"C:\Users\emgap\Downloads\Leonardo_Kino_XL_Generate_a_background_for_a_2D_game_that_has_3.jpg")
    background_image = pygame.transform.scale(background_image, (360, 640))

    left_limit = -140
    right_limit = 360 - 100

    monito_image = pygame.image.load(r"C:\TEC\matemáticas juego\chango_1_preview_rev_1.png")
    monito_image = pygame.transform.scale(monito_image, (200, 200))
    monito_x = 360 // 2 - 25
    monito_y = 640 - 180
    monito_speed = 3.5

    fall_speed = 0.09
    spawn_timer = 0
    spawn_delay = 1500
    object_image = pygame.image.load(r"C:\TEC\matemáticas juego\bananas__preview_rev_1.png")
    object_image = pygame.transform.scale(object_image, (80, 80))

    falling_objects = []
    soluciones = resolver_ecuacion()
    puntos = 0
    oportunidad = False

    def generar_numeros_falsos(soluciones):
        falsos = []
        while len(falsos) < 2:
            falso = random.randint(-20, 20)
            if falso not in soluciones and falso not in falsos:
                falsos.append(falso)
        return falsos

    falsos = generar_numeros_falsos(soluciones)
    ecuacion_imagen = pygame.image.load('ecuacion.png')

    imagenes_bananas = actualizar_imagenes(soluciones, falsos)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                limpiar_imagenes()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            monito_x -= monito_speed
        if keys[pygame.K_RIGHT]:
            monito_x += monito_speed

        if monito_x < left_limit:
            monito_x = left_limit
        elif monito_x > right_limit:
            monito_x = right_limit

        spawn_timer += 1
        if spawn_timer > spawn_delay:
            spawn_timer = 0
            new_x = random.randint(left_limit, right_limit)
            objeto = [new_x, -80, random.choice(soluciones + falsos)]
            falling_objects.append(objeto)

        for obj in falling_objects[:]:
            obj[1] += fall_speed

            if monito_x < obj[0] < monito_x + 200 and monito_y < obj[1] + 30 < monito_y + 200:
                if obj[2] in soluciones:
                    if oportunidad:
                        puntos += 1
                        soluciones = resolver_ecuacion()
                        falsos = generar_numeros_falsos(soluciones)
                        falling_objects.clear()
                        ecuacion_imagen = pygame.image.load('ecuacion.png')
                        imagenes_bananas = actualizar_imagenes(soluciones, falsos)
                        oportunidad = False
                    else:
                        oportunidad = True
                else:
                    # Si es un número falso, simplemente lo elimina sin mostrar mensaje
                    falling_objects.remove(obj)

        for obj in falling_objects:
            if obj[1] >= 640:
                if obj[2] in soluciones:
                    mostrar_texto("¡Perdiste!", 180, 320, red, 50)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    limpiar_imagenes()
                    return
                falling_objects.remove(obj)

        falling_objects = [obj for obj in falling_objects if obj[1] < 640]

        screen.fill(black)
        screen.blit(background_image, (0, 0))
        screen.blit(monito_image, (monito_x, monito_y))

        for i, obj in enumerate(falling_objects):
            if obj[2] in soluciones:
                index = soluciones.index(obj[2])
                screen.blit(imagenes_bananas[index], (obj[0], obj[1]))
            else:
                index = len(soluciones) + falsos.index(obj[2])
                screen.blit(imagenes_bananas[index], (obj[0], obj[1]))

        mostrar_texto(f"Puntos: {puntos}", 180, 90, white, 30)
        screen.blit(ecuacion_imagen, (20, 20))

        pygame.display.flip()

# Ejecutar el juego
juego()
