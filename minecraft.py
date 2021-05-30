import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy

import time
# a change

class CarrierClass:
    pass

global carrier
carrier = CarrierClass()


vertex_shader = """
#version 330
in vec4 position;
void main() {
    gl_Position = position;
}
"""
fragment_shader = """
#version 330
void main() {
    gl_FragColor = vec4(1.0f, 0.0f, 0.0f, 1.0f);
}
"""
shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

VBO = glGenBuffers(1)
glBindBuffers(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, 36, coords, GL_STATIC_DRAW)

vboPos = glGetAttribLocation(shader, "position")
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(position)
glUseProgram(shader)

coords_f64 = [
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0, 0.5, 0.0
]
coords_f32 = numpy.array(coords_f64, dtype = numpy.float32)

def main():
    # see if glfw is even working
    if not glfw.init():
        print("glfw failed lmao")
        return

    # create a window
    carrier.window = glfw.create_window(800, 600, "m i n e c r a f t", None, None)
    if not carrier.window:
        print("window creation failed lmao")
        glfw.terminate()
        return

    glfw.make_context_current(carrier.window)

    glClearColor(0.0, 0.0, 0.0, 1.0)

    # g a m e  l o o p
    while not glfw.window_should_close(carrier.window):
        time.sleep(0.01)
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(carrier.window)

    glfw.terminate()

main()