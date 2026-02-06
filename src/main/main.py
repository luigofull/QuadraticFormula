from manim import *
from MF_Tools import *
from moves import *


class Animation(Scene):
    def construct(self):
        self.add(exp1)
        self.wait()
        
        exp1to2(self)
        exp2to3(self)
        exp3to4(self)
        exp4to5(self)
        exp5to6(self)
        exp6to7(self)
        exp7to8(self)
        exp8to9(self)
        exp9to10(self)
        exp10to11(self)
        exp11to12(self)
        exp12to13(self)
        exp13to14(self)
        exp14to15(self)
        exp15to16(self)
        exp16to17(self)
        exp17to18(self)
        exp18to19(self)
        exp19to20(self)
        exp20to21(self)
        exp21to22(self)
        
        box = SurroundingRectangle(
            exp22, 
            color=YELLOW, 
            buff=0.2  
        )
        
        self.play(Create(box))
        
        self.wait()