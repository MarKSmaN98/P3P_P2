from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("OUR GROUP", font='big'),
            int(screen.height / 2 -8)),
        Cycle(
            screen,
            FigletText("ROCKS!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)

# def demo(screen):
    
#     while True:
#         screen.print_at('Hello world!',
#                         random.randint(0, screen.width), random.randint(0, screen.height),
#                         colour=random.randint(0, screen.colours - 1),
#                         bg=random.randint(0, screen.colours - 1))
#         ev = screen.get_key()
#         if ev in (ord('Q'), ord('q')):
#             return
#         screen.refresh()

#     Screen.wrapper(demo)

demo()

