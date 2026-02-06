# lib imports
from manim import *
from MF_Tools import *

# project imports
import moves as mv
import exps as ex


class Animation(Scene):
    def construct(self):
        self.add(ex.exp1)
        self.wait()
        
        mv.exp1to2(self)
        mv.exp2to3(self)
        mv.exp3to4(self)
        mv.exp4to5(self)
        mv.exp5to6(self)
        mv.exp6to7(self)
        mv.exp7to8(self)
        mv.exp8to9(self)
        mv.exp9to10(self)
        mv.exp10to11(self)
        mv.exp11to12(self)
        mv.exp12to13(self)
        mv.exp13to14(self)
        mv.exp14to15(self)
        mv.exp15to16(self)
        mv.exp16to17(self)
        mv.exp17to18(self)
        mv.exp18to19(self)
        mv.exp19to20(self)
        mv.exp20to21(self)
        mv.exp21to22(self)
        
        box = SurroundingRectangle(
            ex.exp22, 
            color=YELLOW, 
            buff=0.2  
        )
        
        self.play(Create(box))
        
        self.wait()