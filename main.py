import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes

class App:

    def __init__(self):
        pg.init()
        pg.display.set_mode((640, 400), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)
        self.mainLoop()


    def mainLoop(self):
        running = True
        while (running):
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    running = False

            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()

class Triangle:

    def __init__(self):

        #x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            -0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            -0.5, -0.5, 0.0, 0.0, 0.0, 1.0
        )

        self.vertices = np.array(self.vertices, dtype=np.float32) # The second argument determines the datatype stored in the vertices

        self.vertex_count = 3 # Stores n number of vertexes

        self.vao = glGenVertexArrays(1) # determines the meaning of each vertex's number
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1) # vertex buffer object
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexArrayAttrib(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):

        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

if __name__ == "__main__":
    myApp = App()
    