import glfw
import math
from OpenGL.GL import *
import random
import time

x, y = 0, 0
angulo = 0
tam = 0.10
velocidade_inicial = 0.01
velocidade_atual = velocidade_inicial 
velocidade_maxima = 0.05
aceleracao = 0.0003
acelerando = False
tiros = []
velocidade_tiros = 0.02
velocidade_asteroids = 0.02
angulo_asteroids = 0

num_estrelas = 800
vertices_estrelas = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_estrelas)]

num_asteroids = 6
vertices_asteroids = [[random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0, 360)] for _ in range(num_asteroids)]

teclas = { glfw.KEY_W: False,
            glfw.KEY_A: False,
            glfw.KEY_D: False, 
            glfw.KEY_SPACE: False}

def desenha_asteroids():
    for asteroid in vertices_asteroids:
        x, y, _ = asteroid
        glPushMatrix()
        glTranslatef(x, y, 0)
        glRotatef(angulo_asteroids, 0, 0, 1) 
        glColor3f(0.6, 0.6, 0.6) 
        glBegin(GL_POLYGON)
        num_lados = 10
        raio_base = 0.03  

        for i in range(num_lados):
            angulo = 2 * math.pi * i / num_lados
            variacao = 1 + 0.2 * math.sin(i * 2)  
            raio = raio_base * variacao
            vx = raio * math.cos(angulo)
            vy = raio * math.sin(angulo)
            glVertex2f(vx, vy)
        glEnd()
        glPopMatrix()


def desenha_estrelas():
    glPointSize(1) 
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  
    
    for estrela in vertices_estrelas:
        glVertex2f(estrela[0], estrela[1])
    glEnd()

def inicio():
    glClearColor(0, 0, 0.0, 0.0)

def desenha():
    # glLoadIdentity()
    desenha_estrelas()
    desenha_asteroids()

    glPushMatrix()
    glTranslate(x, y, 0)
    glRotatef(angulo, 0, 0, 1)

    glBegin(GL_POLYGON)
    glColor3f(0.8, 0.0, 0.2)  
    glVertex2f(-tam * 0.5, -tam)
    glVertex2f(tam * 0.5, -tam)
    glVertex2f(tam * 0.3, tam * 1.5)
    glVertex2f(-tam * 0.3, tam * 1.5)
    glEnd()
    
    # Janela
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.8, 1.0)  
    glVertex2f(-tam * 0.15, 0.3 * tam)
    glVertex2f(-tam * 0.1, 0.5 * tam) 
    glVertex2f(tam * 0.1, 0.5 * tam )   
    glVertex2f(tam * 0.15, 0.3 * tam )   
    glVertex2f(0.0, 0.2 * tam)   
    glEnd()
    
    # ponta do foguete
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 0.0) 
    glVertex2f(-tam * 0.3, tam * 1.5)
    glVertex2f(tam * 0.3, tam * 1.5)
    glVertex2f(0.0, tam * 2.0)
    glEnd()

    # Asa
    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.2, 0.8) 
    glVertex2f(-tam * 0.6, -tam * 0.4)
    glVertex2f(-tam * 0.4, -tam)
    glVertex2f(-tam * 0.9, -tam * 1.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.2, 0.8)  
    glVertex2f(tam * 0.6, -tam * 0.4)
    glVertex2f(tam * 0.4, -tam)
    glVertex2f(tam * 0.9, -tam * 1.0)
    glEnd()
  
    # Fogo
    if acelerando == True or velocidade_atual > 0.01:  
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.5, 0.0)  
        glVertex2f(-tam * 0.3, -tam)
        glVertex2f(tam * 0.3, -tam)
        glVertex2f(0.0, -tam * 1.5)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 1.0, 0.0)  
        glVertex2f(-tam * 0.2, -tam * 1.1)
        glVertex2f(tam * 0.2, -tam * 1.1)
        glVertex2f(0.0, -tam * 1.8)
        glEnd()

    glPopMatrix() 
        
    glFlush()

def atualizar_aceleracao():
    global x, y
    global angulo, velocidade_inicial, velocidade_atual, velocidade_maxima

    if acelerando:
        velocidade_atual += aceleracao
        if velocidade_atual > velocidade_maxima:
            velocidade_atual = velocidade_maxima
    else:
        if velocidade_atual > velocidade_inicial:
            velocidade_atual -= aceleracao
        if velocidade_atual < velocidade_inicial:
            velocidade_atual = velocidade_inicial

    andar = math.radians(angulo + 90)
    x += math.cos(andar) * velocidade_atual
    y += math.sin(andar) * velocidade_atual
        
    if x < -1 + tam or x > 1 - tam:
        x = x * -1
    if y < -1 + tam or y > 1 - tam:
        y = y * -1
    
    if teclas[glfw.KEY_A]:
        angulo += 2
    if teclas[glfw.KEY_D]:
        angulo -= 2


def desenha_tiros():
    global tiros
    novos_tiros = []
    for tiro in tiros:
        x, y, angulo_tiros = tiro
        angle = math.radians(angulo_tiros + 90)
        x += math.cos(angle) * velocidade_tiros
        y += math.sin(angle) * velocidade_tiros
        
        if y <= 1:
            novos_tiros.append([x,y, angulo_tiros])

        glPushMatrix()
        glTranslate(x, y, 0)
        glRotatef(angulo_tiros, 0, 0, 1)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 0.0)  
        glVertex2f(0.0, tam * 2.2)  
        glVertex2f(0.0, tam * 2.5) 
        glEnd()
        glPopMatrix()
    tiros = novos_tiros

def movimentacao_asteroids():
    global vertices_asteroids, velocidade_asteroids

    for i in range(len(vertices_asteroids)):
        x, y, angulo = vertices_asteroids[i]

        x += velocidade_asteroids * math.cos(math.radians(angulo))
        y += velocidade_asteroids * math.sin(math.radians(angulo))

        if x < -1 or x > 1 or y < -1 or y > 1:
            borda = random.randint(0, 3)

            if borda == 0:  # esquerda
                x = -1
                y = random.uniform(-1, 1)
            elif borda == 1:  # direita
                x = 1
                y = random.uniform(-1, 1)
            elif borda == 2:  # cima
                x = random.uniform(-1, 1)
                y = 1
            else:  # baixo
                x = random.uniform(-1, 1)
                y = -1

        vertices_asteroids[i] = [x, y, angulo]


def teclado(window, key, scancode, action, mods):
    global  acelerando, teclas, tiros, x, y, angulo

    if key in teclas:
        if action == glfw.PRESS:
            teclas[key] = True
        elif action == glfw.RELEASE:
            teclas[key] = False

    if key == glfw.KEY_W:
        if action == glfw.PRESS:
            acelerando = True
        elif action == glfw.RELEASE:
            acelerando = False

    if key == glfw.KEY_SPACE:
        if action == glfw.PRESS:
            tiros.append([x, y, angulo])
 
            
    
def main():
    glfw.init()
    window = glfw.create_window(600, 600, 'Teste GLFW', None, None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, teclado)

    inicio()

    while glfw.window_should_close(window) == False:
        time.sleep(1/30)
        glClear(GL_COLOR_BUFFER_BIT)
        global angulo_asteroids
        angulo_asteroids += 2
        desenha()
        atualizar_aceleracao()
        movimentacao_asteroids()
        desenha_tiros()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


if __name__ == '__main__':
    main()
