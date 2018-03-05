"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Xiaoyu Ma.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(10)

joye = rg.SimpleTurtle('classic')
oliver = rg.SimpleTurtle('turtle')

joye.pen = rg.Pen('black', 5)
oliver.pen = rg.Pen('red', 5)

joye.speed = 20
joye.pen_up()
joye.forward(150)
joye.left(90)
joye.pen_down()

oliver.speed = 15
oliver.pen_up()
oliver.forward(100)
oliver.left(90)
oliver.backward(50)
oliver.pen_down()

for i in range(3):
    joye.draw_circle(50)
    joye.pen_up()
    joye.right(90)
    joye.backward(100)
    joye.left(90)
    joye.pen_down()

for k in range(2):
    oliver.draw_circle(50)
    oliver.pen_up()
    oliver.left(90)
    oliver.forward(100)
    oliver.right(90)
    oliver.pen_down()

window.close_on_mouse_click()




