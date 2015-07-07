from IPython.display import display
from IPython.html.widgets import interact
import sympy

sympy.init_printing(use_latex='mathjax')

@interact
def factor(n=10):
    display(sympy.factor(x**n-1))
