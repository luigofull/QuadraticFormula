from manim import *
from MF_Tools import *
from formula_steps import *

  
def exp1to2(self):
    self.play(
        TransformByGlyphMap(
            exp1, 
            exp2,
            
            # devide by a
            ([0],[5,10]),
            ([],[4,9])
        ), 
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp2to3(self):
    self.play(
        TransformByGlyphMap(
            exp2,
            exp3,
            
            # - c/a
            ([7,8,9,10], [8,9,10,11]),
            ([12], [])
        ), 
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp3to4(self):
    self.play(
        TransformByGlyphMap(
            exp3,
            exp4,
            
            # +
            ([2], [2]),
            ([2], [8]),
            
            # division
            ([4], [4]),
            ([4], [10]),
            
            # b
            ([3], [3]),
            ([3], [9]),
            
            # x
            ([6], [7]),
            ([6], [13]),
            
            # 2a
            ([5], [6]),
            ([5], [12]),
            ([5], [5]), 
            ([5], [11]),    
                        
            # =
            ([7], [14]),
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp4to5(self):
    self.play(
        TransformByGlyphMap(
            exp4,
            exp5,
            
            # + & ()
            ([], [14]),
            ([], [*ir(15,21)]),
            ([], [*ir(23,29)])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    

def exp5to6(self):
    self.play(
        TransformByGlyphMap(
            exp5,
            exp6,
            
            # ()^2
            ([29], [24], {"path_arc":PI}),
            ([29], [28], {"path_arc":PI}),
            
            # 2^2
            ([26], [26]),
            
            # !()
            ([23], []),
            ([28], []),
            
            
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp6to7(self):
    self.play(
    TransformByGlyphMap(
            exp6,
            exp7,
            
            # add -1
            ([], [30,31]),
        ),
        run_time=1.5
    )
    self.wait(0.85)

    
def exp7to8(self):
    self.play(
    TransformByGlyphMap(
            exp7,
            exp8,
            
            # 1 to 4a/4a
            ([30], (30,31)),
            ([30], [33,34]),
            ([], [32])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp8to9(self):
    self.play(
    TransformByGlyphMap(
            exp8,
            exp9,
            
            #  4ac/4a^2
            ([30,31,36], [30,31,32]),
            ([32,37], [33]),
            ([35], []),
            ([33], [34]),
            ([34,38], [35]),
            ([], [36])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp9to10(self):
    self.play(
    TransformByGlyphMap(
            exp9,
            exp10,
            
            ([23,24], [23,24]),
            ([30,31,32], [26,27,28]),
            ([29], [25]),
            ([25,33], [29]),
            
            ([34,35,36], [30,31,32]),
            ([26,27,28], [30,31,32])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp10to11(self):
    self.play(
    TransformByGlyphMap(
            exp10,
            exp11,
            
            # x^2 to x * x
            ([0], [0]),
            ([0], [2]),
            ([1], []),
            ([], [1]),
            
            # (b/2a)^2 to b/2a * b/2a
            ([16,17,18,19], [16,17,18,19]),
            ([], [20]),
            ([16,17,18,19], [21,22,23,24]),
            
            ([15,20], []),
            ([21], []),
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp11to12(self):
    self.play(
    TransformByGlyphMap(
            exp11,
            exp12,
            
            # ()
            ([*ir(0,8)], [*ir(1,9)]),
            ([], [0,10]),
            
            ([*ir(10,24)], [*ir(13,27)]),
            ([], [12,28])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp12to13(self):
    self.play(
    TransformByGlyphMap(
            exp12,
            exp13,
            
            # ()
            ([0], [1]),
            ([10], [8]),
            ([12], [14]),
            ([28], [21]),
            
            ([2], []),
            ([23], []),
            ([1], [0]),
            ([9], [0]),
            
            ([*ir(13,16)], [*ir(10,13)]),
            ([*ir(24,27)], [*ir(10,13)])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp13to14(self):
    self.play(
    TransformByGlyphMap(
            exp13,
            exp14,
            
            # ()
            ([*ir(0,21)], [*ir(1,22)]),
            ([], [0,23]),
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp14to15(self):
    self.play(
    TransformByGlyphMap(
            exp14,
            exp15,
            
            # ()
            ([*ir(2,9)], [*ir(0,7)]),
            ([*ir(15,22)], [*ir(0,7)]),
            
            ([0], [9]),
            ([1], [10]),
            ([10], [11]),
            ([*ir(11,14)], [*ir(12,15)]),
            ([23], [16]),
            
            ([], [8])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp15to16(self):
    self.play(
    TransformByGlyphMap(
            exp15,
            exp16,
            
            # ()^2
            ([8], []),
            ([], [8]),
            ([*ir(0,7)], [*ir(0,7)]),
            ([*ir(9,16)], [*ir(0,7)])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    

def exp16to17(self):
    self.play(
    TransformByGlyphMap(
            exp16,
            exp17,
            
            # sqrt()=sqrt()
            ([], [0,1]),
            ([], [12]),
            ([], [13,14])
        ),
        run_time=1.5
    )
    self.wait(0.85)



def exp17to18(self):
    self.play(
    TransformByGlyphMap(
            exp17,
            exp18,
            
            # =sqrt()
            ([0,1,2,9,10], [])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    

def exp18to19(self):
    self.play(
    TransformByGlyphMap(
            exp18,
            exp19,
            
            # =sqrt()/sqrt()
            ([8,9], [8,9]),
            ([8,9], [17,18])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    
    
def exp19to20(self):
    self.play(
    TransformByGlyphMap(
            exp19,
            exp20,
            
            # sqrt()/2a
            ([17,18,21], []),
            ([19], [17])
        ),
        run_time=1.5
    )
    self.wait(0.85)
   
    
def exp20to21(self):
    self.play(
    TransformByGlyphMap(
            exp20,
            exp21,
            
            # b/2a to -b/2a
            ([1], [2]),
            ([*ir(2,5)], [*ir(3,6)])
        ),
        run_time=1.5
    )
    self.wait(0.85)
    

def exp21to22(self):
    self.play(
    TransformByGlyphMap(
            exp21,
            exp22,
            
            # complite
            ([2], [2]),
            ([3], [3]),
            ([7], [4]),
            ([4,16], [13]),
            
            ([5,6], [14,15]),
            ([17,18], [14,15])
        ),
        run_time=1.5
    )
    self.wait(0.85)