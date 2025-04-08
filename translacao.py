import glfw
import math
from OpenGL.GL import *
import random

x, y = 0, 0
angulo = 0
tam = 0.10
mov = 0.01
aceleracao = 0.0003

num_estrelas = 50
vertices_estrelas = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range (num_estrelas)]

def inicio():
    glClearColor(0, 0, 0.3, 1)

def desenha():
    # glLoadIdentity()
    glPushMatrix()
    glTranslate(x, y, 0)
    glRotatef(angulo, 0, 0, 1)

    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.0, 0.5)
    glVertex2f(-tam, -tam)
    glVertex2f(tam, -tam) 
    glVertex2f(0.0, tam)   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.2, 0.0, 0.5)
    glVertex2f(-tam * 0.15, 0.3 * tam)
    glVertex2f(-tam * 0.1, 0.5 * tam) 
    glVertex2f(tam * 0.1, 0.5 * tam )   
    glVertex2f(tam * 0.15, 0.3 * tam )   
    glVertex2f(0.0, 0.2 * tam)   
    glEnd()

    
    glBegin(GL_POINTS)  
    

    glPopMatrix() 

    for x,y in vertices_estrelas:
        
    glFlush()

def teclado(window, key, scancode, action, mods):

    global x, y 
    global angulo, mov

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
           andar = math.radians(angulo + 90)
           x += math.cos(andar) * mov
           y += math.sin(andar) * mov 

           mov+=aceleracao

        if key == glfw.KEY_A:
            angulo+=10
        if key == glfw.KEY_D:
            angulo+=-10

    
def main():
    glfw.init()
    window = glfw.create_window(600, 600, 'Teste GLFW', None, None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, teclado)

    inicio()

    while glfw.window_should_close(window) == False:
        glClear(GL_COLOR_BUFFER_BIT)
        desenha()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


if __name__ == '__main__':
    main()