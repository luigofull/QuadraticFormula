from manim import *


basicFormula = SingleStringMathTex(
    r"ax^{2}+bx+c=0"
).scale(0.83)

formulaStep2 = SingleStringMathTex(
    r"x^{2}+\frac{b}{a}x+\frac{c}{a}=0"
).scale(0.83)

formulaStep3 = SingleStringMathTex(
    r"x^{2}+\frac{b}{a}x=-\frac{c}{a}"
).scale(0.83)

formulaStep4 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x=-\frac{c}{a}"
).scale(0.83)

formulaStep5 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\left( \frac{b}{2a} \right)^{2}-\frac{c}{a}"
).scale(0.83)

formulaStep6 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\frac{b^{2}}{4a^{2}}-\frac{c}{a}"
).scale(0.83)

formulaStep7 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\frac{b^{2}}{4a^{2}}-1\cdot \frac{c}{a}"
).scale(0.83)

formulaStep8 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\frac{b^{2}}{4a^{2}}-\frac{4a}{4a}\cdot \frac{c}{a}"
).scale(0.83)

formulaStep9 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\frac{b^{2}}{4a^{2}}-\frac{4ac}{4a^{2}}"
).scale(0.83)

formulaStep10 = SingleStringMathTex(
    r"x^{2}+\frac{b}{2a}x+\frac{b}{2a}x+\left( \frac{b}{2a} \right)^{2}=\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep11 = SingleStringMathTex(
    r"x\cdot x+\frac{b}{2a}x+\frac{b}{2a}x+\frac{b}{2a}\cdot \frac{b}{2a}=\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep12 = SingleStringMathTex(
    r"\left( x\cdot x+\frac{b}{2a}x \right)+\left( \frac{b}{2a}x+\frac{b}{2a}\cdot \frac{b}{2a} \right)=\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep13 = SingleStringMathTex(
    r"x\left( x+\frac{b}{2a} \right)+\frac{b}{2a}\left(x+\frac{b}{2a} \right)=\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep14 = SingleStringMathTex(
    r"\left( x\left( x+\frac{b}{2a} \right)+\frac{b}{2a}\left(x+\frac{b}{2a} \right) \right)=\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep15 = SingleStringMathTex(
    r"\left( x+\frac{b}{2a} \right)\cdot \left(x+\frac{b}{2a} \right) =\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep16 = SingleStringMathTex(
    r"\left( x+\frac{b}{2a} \right)^{2} =\frac{b^{2}-4ac}{4a^{2}}"
).scale(0.83)

formulaStep17 = SingleStringMathTex(
    r"x+\frac{b}{2a} =\pm \sqrt{\frac{b^{2}-4ac}{4a^{2}}}"
).scale(0.83)

formulaStep18 = SingleStringMathTex(
    r"x+\frac{b}{2a} =\pm \frac{\sqrt{b^{2}-4ac}}{\sqrt{4a^{2}}}"
).scale(0.83)

formulaStep19 = SingleStringMathTex(
    r"x+\frac{b}{2a} =\pm \frac{\sqrt{b^{2}-4ac}}{2a}"
).scale(0.83)

formulaStep20 = SingleStringMathTex(
    r"x=-\frac{b}{2a}\pm \frac{\sqrt{b^{2}-4ac}}{2a}"
).scale(0.83)

formulaStep21 = SingleStringMathTex(
    r"x =\frac{-b\pm \sqrt{b^{2}-4ac}}{2a}"
).scale(0.83)