import glfw
from OpenGL.GL import *

x, y = 0, 0
angulo = 0
tam = 0.10

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

    glPopMatrix()

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.5, 0.0)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, 0.75) 
    glVertex2f(0.75, 0.75)   
    glVertex2f(0.75, 0.5) 
    glEnd()

    glFlush()

def teclado(window, key, scancode, action, mods):

    global x, y 
    global angulo

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP and y <= 1 - 0.15:
           y+=0.1
        if key == glfw.KEY_DOWN and y >= -1 + 0.15:
            y+=-0.1
        if key == glfw.KEY_LEFT and x >= -1 + 0.15:
           x+=-0.1
        if key == glfw.KEY_RIGHT and x <= 1 - 0.15:
           x+=0.1

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