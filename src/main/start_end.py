from manim import *
from formula_steps import *


def start(self):
    text_obj = Text("Why?", font_size=36)
    text_obj.next_to(exp0, UP, buff=0.6)
    exp0s = exp0[0].split()

    # colorize
    exp0s[10].set_color(YELLOW)
    exp0s[11].set_color(YELLOW)

    self.play(
        Write(text_obj),
        Write(exp0),
        run_time=2
    )
    self.wait()

    self.play(
        FadeOut(text_obj),
        FadeOut(exp0),
        run_time=1.5
    )
    self.wait(0.5)

    self.play(Write(exp1))

    self.wait()


def end(self):
    box = SurroundingRectangle(
        exp22, 
        color=YELLOW, 
        buff=0.3  
    )

    self.play(Create(box))

    self.wait(3)